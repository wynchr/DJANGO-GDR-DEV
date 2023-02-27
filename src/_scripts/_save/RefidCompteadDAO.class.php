<?php
require_once $BASEDIR . 'classes/ConnectionDB.class.php';
require_once $BASEDIR . 'classes/Traduction.class.php';
require_once $BASEDIR . 'classes/RefidGestionException.php';
require_once $BASEDIR . 'classes/Modeles/RefidComptead.class.php';
require_once $BASEDIR . 'classes/Map/RefidCompteadMap.class.php';

if (class_exists('RefidCompteadDAO')) {
    return true;
}

class RefidCompteadDAO
{
    private $table = 'REFID_COMPTEAD';
    private $db;
    private $typedb = 'oracle';
    private $prefix_l = '';
    private $DBLA = 'informatique';
    private $langueUser = 'FR';
    private $traduction;
    private $error;
    private $txterror;
    private $nhop = 26;
    private $objetUserAcces;

    public function __construct($objUserAcces)
    {
        $this->objetUserAcces = $objUserAcces;
        $this->langueUser = $this->objetUserAcces->getLangueUser();
        if ($this->langueUser == '') {
            $this->langueUser = 'FR';
        }

        $this->traduction = new Traduction($this->langueUser);
        if ($this->langueUser == 'NL') {
            $this->prefix_l = '_NL';
        }

        $this->nhop = $this->objetUserAcces->getViewHopital();
    }
    public function getError()
    {
        return $this->error;
    }
    public function getTxtError()
    {
        return $this->txterror;
    }
    public function getChamps()
    {
        return $this->champs;
    }
    public function getTable()
    {
        return $this->table;
    }
    public function getDb()
    {
        return $this->db;
    }
    public function add($objet)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query('insert', $this->table, ConnectionDB::builMapRequest($objet, RefidCompteAdMap::getTabMapping(), RefidCompteAdMap::getNoAddField()));
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            } else {
                $this->db->Exec_Query('select', "refid_comptead", RefidCompteadMap::getTabChamps(), " IDCOMPTEAD = (SELECT max(idcomptead)
							FROM REFID_COMPTEAD
							WHERE IDCOLLABORATION_FK =" . $objet->getIdcollaborationfk() . ")");
                if ($this->db->DataBase->Errno == 0) {
                    if ($this->db->Fetch()) {
                        $data = array_change_key_case($this->db->DataBase->Get_Record());
                        $o = new RefidComptead();
                        $o = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                        //creation du mot de passe provisoire
                        $o = $this->generatePassword($o);
                        if ($this->getError() == 1) {
                            $this->db->Exec_Query_SQL("update refid_individu set statutaction=5 where idindividu=" . $o->getIdindividufk());
                            throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']: add pwd comptead', 2);
                        }
                        //Tool::debug($data['refid_comptead_pwdtmp']->load());
                    }
                }
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function updateCompteAdByCollaboration($idc, $tab)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_QUERY("update", $this->table, $tab, "idcomptead in (
										select distinct  idcomptead
										FROM REFID_COMPTEAD rc JOIN REFID_COLLABORATION rc2 ON rc.IDCOLLABORATION_FK =rc2.IDCOLLABORATION
											 JOIN REFID_INDIVIDU ri ON rc2.IDINDIVIDU_FK =ri.IDINDIVIDU
										WHERE rc.invalide IS NULL AND rc2.invalide IS NULL AND  rc.flag_archive is null  and rc2.idcollaboration='" . $idc . "')");
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function updateCompteAdByIdindividu($idindividu, $tab)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            //on recupere les informations li�e a la collaboration�

            $this->db->Exec_QUERY("update", "$this->table", $tab, "idcomptead in (
										select distinct  upper(username)
										FROM REFID_COMPTEAD rc JOIN REFID_COLLABORATION rc2 ON rc.IDCOLLABORATION_FK =rc2.IDCOLLABORATION
											 JOIN REFID_INDIVIDU ri ON rc2.IDINDIVIDU_FK =ri.IDINDIVIDU
										WHERE rc.invalide IS NULL AND rc2.invalide IS NULL AND  rc.flag_archive is null  and rc2.idIndividu_fk='" . $idindividu . "')");
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function update($objet)
    {
        RefidGestionException::toException();
        try {
            $tab['date_debut'] = $objet->getDatedebut();
            $tab['date_fin'] = $objet->getDatefin();
            //$tab['username'] =$objet->getUsername();
            //$tab['ad_cible'] =$objet->getAdcible();
            //$tab['ou_cible'] =$objet->getOucible();
            $tab['update_date'] = $objet->getUpdatedate();
            $tab['updateby'] = $objet->getUpdateby();
            $tab['idcollaboration_fk'] = $objet->getIdcollaborationfk();
            $tab['idindividu_fk'] = $objet->getIdindividufk();
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query('update', $this->table, $tab, "idcomptead='" . $objet->getIdcomptead() . "'");
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function get($idcomptead)
    {
        RefidGestionException::toException();
        try {
            $o = null;
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query('select', $this->table . " refid_comptead  left JOIN refid_individu refid_individu ON refid_comptead.idindividu_fk = refid_individu.idindividu left JOIN refid_collaboration refid_collaboration ON refid_comptead.idcollaboration_fk = refid_collaboration.idcollaboration", array_merge(RefidCompteadMap::getTabChamps(), RefidIndividuMap::getTabChamps(), RefidCollaborationMap::getTabChamps()), "idcomptead='" . $idcomptead . "'");
            if ($this->db->DataBase->Errno == 0) {
                if ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->DataBase->Get_Record());
                    $o = new RefidComptead();
                    $o = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                    $oRefidIndividu = new RefidIndividu();
                    $oRefidIndividu = ConnectionDB::buildObject($oRefidIndividu, RefidIndividuMap::getTabMapping(), $data);
                    $o->setObjetRefidIndividu($oRefidIndividu);
                    $oRefidCollaboration = new RefidCollaboration();
                    $oRefidCollaboration = ConnectionDB::buildObject($oRefidCollaboration, RefidCollaborationMap::getTabMapping(), $data);
                    $o->setObjetRefidCollaboration($oRefidCollaboration);
                    //Tool::debug($o);
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $o;
    }
    public function countlisting($params = array())
    {
        $nb = 0;
        RefidGestionException::toException();
        try {
            $where = '';
            if ($params['rechercher'] != '') {
                if (is_numeric($params['rechercher'])) {
                    $where = " where (refid_comptead.idcomptead=" . $params['rechercher'] . "  or refid_comptead.flag_archive=" . $params['rechercher'] . "  or refid_comptead.idcollaboration_fk=" . $params['rechercher'] . "  or refid_comptead.idindividu_fk=" . $params['rechercher'] . " )";
                } else {
                    $where = " where ( upper(refid_comptead.username) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.sid) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.ad_cible) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.ou_cible) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.invalideur) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.createby) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.updateby) like upper('%" . $params['rechercher'] . "%') )";
                }
            } //count
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query_SQL(" select count(*) as nb
	            from (
	            select ROW_NUMBER() OVER (ORDER BY idcomptead asc) R, idcomptead
	            from REFID_COMPTEAD refid_comptead  left JOIN refid_individu refid_individu ON refid_comptead.idindividu_fk = refid_individu.idindividu left JOIN refid_collaboration refid_collaboration ON refid_comptead.idcollaboration_fk = refid_collaboration.idcollaboration" . $where . ")");
            if ($this->db->DataBase->Errno == 0) {
                if ($this->db->Fetch()) {
                    $nb = $this->db->Get_Field('nb');
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $nb;
    }
    public function listing($page = 1, $pas = 10, $params = array())
    { //OK
        $tab = array();
        RefidGestionException::toException();
        try {
            if ($page > 1) {
                $avant = $page - 1;
                $avant = $avant * $pas;
            } else {
                $avant = 0;
            }

            $apres = $page * $pas;
            $where = '';
            if ($params['rechercher'] != '') {
                if (is_numeric($params['rechercher'])) {
                    $where = " where (refid_comptead.idcomptead=" . $params['rechercher'] . "  or refid_comptead.flag_archive=" . $params['rechercher'] . "  or refid_comptead.idcollaboration_fk=" . $params['rechercher'] . "  or refid_comptead.idindividu_fk=" . $params['rechercher'] . " )";
                } else {
                    $where = " where ( upper(refid_comptead.username) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.sid) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.ad_cible) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.ou_cible) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.invalideur) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.createby) like upper('%" . $params['rechercher'] . "%') or upper(refid_comptead.updateby) like upper('%" . $params['rechercher'] . "%') )";
                }
            } //count
            $dtmp = array_merge(RefidCompteadMap::getTabChamps(), RefidIndividuMap::getTabChamps(), RefidCollaborationMap::getTabChamps());
            $datamap = implode(",", array_keys($dtmp));
            unset($dtmp);
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query_SQL("select *
            	from (select ROW_NUMBER() OVER (ORDER BY idcomptead)  R," . $datamap . "
                	 from " . $this->table . " refid_comptead  left JOIN refid_individu refid_individu ON refid_comptead.idindividu_fk = refid_individu.idindividu left JOIN refid_collaboration refid_collaboration ON refid_comptead.idcollaboration_fk = refid_collaboration.idcollaboration
						 " . $where . ") WHERE R >=" . $avant . " and R<=" . $apres);
            if ($this->db->DataBase->Errno == 0) {
                while ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->Get_Record());
                    $o = new RefidComptead();
                    $oRefidIndividu = new RefidIndividu();
                    $oRefidIndividu = ConnectionDB::buildObject($oRefidIndividu, RefidIndividuMap::getTabMapping(), $data);
                    $o->setObjetRefidIndividu($oRefidIndividu);
                    $oRefidCollaboration = new RefidCollaboration();
                    $oRefidCollaboration = ConnectionDB::buildObject($oRefidCollaboration, RefidCollaborationMap::getTabMapping(), $data);
                    $o->setObjetRefidCollaboration($oRefidCollaboration);
                    $cle = strtolower($this->table . '_idcomptead');
                    $tab[$data[$cle]] = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $tab;
    }
    public function listeOption()
    { //OK
        $tab = array();
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query("select", $this->table, RefidCompteadMap::getTabChamps());
            if ($this->db->DataBase->Errno == 0) {
                while ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->Get_Record());
                    $o = new RefidComptead();

                    $cle = strtolower($this->table . '_idcomptead');
                    $tab[$data[$cle]] = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $tab;
    }
    public function active($idcomptead, $actif = 1)
    {
        $this->error = 0;
        $this->txterror = '';
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            if ($actif == 1) {
                $this->db->Exec_Query_SQL("update " . $this->table . " set  statut='DESACTIVER', inactifdate=TO_DATE('" . trim(date('d/m/Y H:i:s')) . "','DD/MM/YYYYHH24:MI:SS')where idcomptead='" . $idcomptead . "'");
            } else {
                $this->db->Exec_Query_SQL("update " . $this->table . " set statut='ACTIF' ,
			inactifdate='' where idcomptead='" . $idcomptead . "'");
            }

            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']' . $this->traduction->getError("err2"), 2);
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::Stop();
    }
    public function invalide($idcomptead, $actif = 1)
    {
        $this->error = 0;
        $this->txterror = '';
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            if ($actif == 1) {
                $this->db->Exec_Query_SQL("update " . $this->table . " set  statut='DELETE', inactifdate=TO_DATE('" . trim(date('d/m/Y H:i:s')) . "','DD/MM/YYYYHH24:MI:SS'), invalide=TO_DATE('" . trim(date('d/m/Y H:i:s')) . "','DD/MM/YYYYHH24:MI:SS') where idcomptead='" . $idcomptead . "'");
            } else {
                $this->db->Exec_Query_SQL("update " . $this->table . " set statut='DESACTIVER' , inactifdate=TO_DATE('" . trim(date('d/m/Y H:i:s')) . "','DD/MM/YYYYHH24:MI:SS'),invalide='' where idcomptead='" . $idcomptead . "'");
            }

            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']' . $this->traduction->getError("err2"), 2);
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::Stop();
    }
    public function listByIndividuActifCompte($idIndividu)
    {
        RefidGestionException::toException();
        try {
            $o = null;
            $taba = array();
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query('select', " refid_Individu refid_Individu
			left JOIN refid_langue refid_langue ON refid_Individu.langue_parlee_institution = refid_langue.idlangue
			left JOIN refid_sexe refid_sexe ON refid_Individu.sexe = refid_sexe.code
			left JOIN refid_qualite refid_qualite ON refid_Individu.qualite = refid_qualite.idqualite
			left join refid_population refid_population on refid_individu.idpopulation_fk = refid_population.idpopulation
			left join REFID_CATEGORIE_PROFESSIONNELLE REFID_CATEGORIE_PROFESSIONNELLE on refid_individu.idcatprof = REFID_CATEGORIE_PROFESSIONNELLE.idcatprof
			JOIN refid_comptead ON refid_comptead.idIndividu_fk = refid_Individu.idIndividu
			left JOIN refid_collaboration refid_collaboration ON refid_collaboration.idcollaboration = refid_comptead.idcollaboration_fk",
                array_merge(RefidLangueMap::getTabChamps(), RefidSexeMap::getTabChamps(), RefidQualiteMap::getTabChamps(), RefidPopulationMap::getTabChamps(), RefidCategorieProfessionnelleMap::getTabChamps(), RefidCompteadMap::getTabChamps(), RefidIndividuMap::getTabChamps(), RefidCollaborationMap::getTabChamps()), "flag_archive is null  and refid_comptead.idIndividu_fk='" . $idIndividu . "'");
            if ($this->db->DataBase->Errno == 0) {
                while ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->DataBase->Get_Record());
                    $o = new RefidComptead();
                    //Tool::debug($data);
                    $o = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                    $oRefidIndividu = new RefidIndividu();
                    $oRefidIndividu = ConnectionDB::buildObject($oRefidIndividu, RefidIndividuMap::getTabMapping(), $data);
                    $oRefidLangue = new RefidLangue();
                    $oRefidLangue = ConnectionDB::buildObject($oRefidLangue, RefidLangueMap::getTabMapping(), $data);
                    $oRefidIndividu->setObjetRefidLangue($oRefidLangue);
                    $oRefidSexe = new RefidSexe();
                    $oRefidSexe = ConnectionDB::buildObject($oRefidSexe, RefidSexeMap::getTabMapping(), $data);
                    $oRefidIndividu->setObjetRefidSexe($oRefidSexe);
                    $oRefidQualite = new RefidQualite();
                    $oRefidQualite = ConnectionDB::buildObject($oRefidQualite, RefidQualiteMap::getTabMapping(), $data);
                    $oRefidIndividu->setObjetRefidQualite($oRefidQualite);
                    $oRefidPopulation = new RefidPopulation();
                    $oRefidPopulation = ConnectionDB::buildObject($oRefidPopulation, RefidPopulationMap::getTabMapping(), $data);
                    $oRefidIndividu->setObjetRefidPopulation($oRefidPopulation);
                    $oRefidCatprof = new RefidCategorieProfessionnelle();
                    $oRefidCatprof = ConnectionDB::buildObject($oRefidCatprof, RefidCategorieProfessionnelleMap::getTabMapping(), $data);
                    $oRefidIndividu->setObjetRefidCategorieProfessionnelle($oRefidCatprof);
                    $o->setObjetRefidIndividu($oRefidIndividu);
                    $oRefidCollaboration = new RefidCollaboration();
                    $oRefidCollaboration = ConnectionDB::buildObject($oRefidCollaboration, RefidCollaborationMap::getTabMapping(), $data);
                    $o->setObjetRefidCollaboration($oRefidCollaboration);
                    $taba[$o->getIdcomptead()] = $o;
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        //Tool::debug($taba);
        return $taba;
    }
    public function listHistorByIndividu($idIndividu)
    {
        RefidGestionException::toException();
        try {
            $o = null;
            $tab = array();
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query('select', "historique_refid_comptead refid_comptead   JOIN refid_Individu refid_Individu ON refid_comptead.idIndividu_fk = refid_Individu.idIndividu
			left JOIN refid_collaboration refid_collaboration ON refid_collaboration.idcollaboration = refid_comptead.idcollaboration_fk",
                array_merge(array("TO_CHAR(refid_comptead.archive_date,'DD/MM/YYYY') as archive_date" => ""), RefidCompteadMap::getTabChamps(), RefidIndividuMap::getTabChamps(), RefidCollaborationMap::getTabChamps()), "refid_comptead.idIndividu_fk='" . $idIndividu . "'");
            if ($this->db->DataBase->Errno == 0) {
                while ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->DataBase->Get_Record());
                    $o = new RefidComptead();
                    $o = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                    $o->setArchivedate($data['archive_date']);

                    $oRefidIndividu = new RefidIndividu();
                    $oRefidIndividu = ConnectionDB::buildObject($oRefidIndividu, RefidIndividuMap::getTabMapping(), $data);
                    $o->setObjetRefidIndividu($oRefidIndividu);
                    $oRefidCollaboration = new RefidCollaboration();
                    $oRefidCollaboration = ConnectionDB::buildObject($oRefidCollaboration, RefidCollaborationMap::getTabMapping(), $data);
                    $o->setObjetRefidCollaboration($oRefidCollaboration);
                    $tab[$o->getIdcomptead()] = $o;
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $tab;
    }
    public function listByCollaboration($idco)
    {
        RefidGestionException::toException();
        try {
            $o = null;
            $tab = array();
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query('select', $this->table . " refid_comptead   JOIN refid_Individu refid_Individu ON refid_comptead.idIndividu_fk = refid_Individu.idIndividu
			left JOIN refid_collaboration refid_collaboration ON refid_collaboration.idcollaboration = refid_comptead.idcollaboration_fk",
                array_merge(RefidCompteadMap::getTabChamps(), RefidIndividuMap::getTabChamps(), RefidCollaborationMap::getTabChamps()), "refid_comptead.idcollaboration_fk='" . $idco . "'");
            if ($this->db->DataBase->Errno == 0) {
                while ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->DataBase->Get_Record());
                    $o = new RefidComptead();
                    $o = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                    $oRefidIndividu = new RefidIndividu();
                    $oRefidIndividu = ConnectionDB::buildObject($oRefidIndividu, RefidIndividuMap::getTabMapping(), $data);
                    $o->setObjetRefidIndividu($oRefidIndividu);
                    $oRefidCollaboration = new RefidCollaboration();
                    $oRefidCollaboration = ConnectionDB::buildObject($oRefidCollaboration, RefidCollaborationMap::getTabMapping(), $data);
                    $o->setObjetRefidCollaboration($oRefidCollaboration);
                    //nb prolongation
                    $dc = ConnectionDB::getConnection($this->typedb, $this->DBLA);
                    $dc->Exec_Query_SQL("SELECT idcomptead,count(DISTINCT idprolongation) as nb
										FROM REFID_COMPTEAD rc  JOIN REFID_PROLONGATION rp ON rc.IDCOMPTEAD = rp.IDCOMPTEAD_FK
										WHERE rc.INVALIDE  IS NULL AND rp.INVALIDE  IS NULL  and rc.idcomptead='" . $o->getIdcomptead() . "'
										GROUP BY IDCOMPTEAD ");
                    if ($dc->DataBase->Errno == 0) {
                        while ($dc->Fetch()) {
                            $o->setNbProlongation($dc->Get_Field("nb"));
                        }
                    }
                    $tab[$o->getIdcomptead()] = $o;
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $tab;
    }
    public function getNombreCompteAdByIndividu($idIndividu)
    {
        RefidGestionException::toException();
        try {
            $nb = 0;
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query_SQL("SELECT COUNT(idcomptead) as nb FROM(
										SELECT idcomptead  FROM REFID_COMPTEAD rc
										WHERE IDINDIVIDU_FK =" . $idIndividu . " AND INVALIDE  IS null
										UNION
										SELECT idcomptead FROM HISTORIQUE_REFID_COMPTEAD
										WHERE IDINDIVIDU_FK =" . $idIndividu . " AND invalide IS null)");
            if ($this->db->DataBase->Errno == 0) {
                if ($this->db->Fetch()) {
                    $nb = $this->db->Get_Field("nb");
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $nb;
    }
    public function generatePassword($o)
    {
        $tab = array();
        RefidGestionException::toException();
        try {
            $chaine = "mnoTUzS567-8kVvwxy9WXYZRNCDEFrslq41GtuaHIJK-pOPQA23LcdefghiBMb-j0";
            srand((double) microtime() * 1000000);
            $pass = '';
            for ($i = 0; $i < 12; $i++) {
                $pass .= $chaine[rand() % strlen($chaine)];
            }
            $base64 = base64_encode($pass);
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $sql = "update  refid_comptead set pwdtmp=EMPTY_CLOB()  where idcomptead=" . $o->getIdcomptead() . " RETURNING pwdtmp INTO :pwdtmp";
            $this->db->DataBase->connect();
            $stmt = oci_parse($this->db->DataBase->Link_ID, $sql);
            // Creates an "empty" OCI-Lob object to bind to the locator
            $myLOB = oci_new_descriptor($this->db->DataBase->Link_ID, OCI_D_LOB);
            // Bind the returned Oracle LOB locator to the PHP LOB object
            oci_bind_by_name($stmt, ":pwdtmp", $myLOB, -1, OCI_B_CLOB);
            // Execute the statement using , OCI_DEFAULT - as a transaction
            oci_execute($stmt, OCI_DEFAULT) or die("Unable to execute query\n");
            // Now save a value to the LOB
            if (!$myLOB->save($base64)) {
                // On error, rollback the transaction
                oci_rollback($this->db->DataBase->Link_ID);
            } else {
                // On success, commit the transaction
                oci_commit($this->db->DataBase->Link_ID);
            }
            // Free resources
            oci_free_statement($stmt);
            $myLOB->free();
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            } else {
                $o->setPwdtmp($base64);
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $o;
    }
    public function provisionningTable($oCompteAd, $env, $action)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            //on recupere les informations li�e a la collaboration
            $obc = new RefidCompteAdDAO($this->objetUserAcces);
            $objetcolDAO = new RefidCollaborationDAO($this->objetUserAcces);
            $oCollaboration = $objetcolDAO->get($oCompteAd->getIdcollaborationfk());
            $objetIndDAO = new RefidIndividuDAO($this->objetUserAcces);
            $oIndividu = $objetIndDAO->getSignalitique($oCollaboration->getIdindividufk());
            $objetLocalisation = new RefidLocalisationDAO($this->objetUserAcces);
            $site = $objetLocalisation->getSiteProv($oCompteAd->getIdcollaborationfk());
            $objetAffectationDAO = new RefidAffectationDAO($this->objetUserAcces);
            $oAffectation = $objetAffectationDAO->getAffectationByCollaboration($oCollaboration->getIdcollaboration());
            $objetAffectationGroupeADDAO = new RefidAffectationGroupeADDAO($this->objetUserAcces);
            $groupe = $objetAffectationGroupeADDAO->getGroupeProv($oCollaboration->getIdcollaboration(), 'Security', $env);
            $liste = $objetAffectationGroupeADDAO->getGroupeProv($oCollaboration->getIdcollaboration(), 'Distribution', $env);
            //$tab["TELEPHONENUMBER"]=$oAffectation->telephone_fixe;
            $tab["SAMACCOUNTNAME"] = $oCompteAd->getUsername();
            $tab["SN"] = strtoupper($oIndividu->getNomUsuel());
            $tab["GIVENNAME"] = ucfirst($oIndividu->getPrenomUsuel());
            if ($oCompteAd->getPwdtmp() != "") {
                $tab["PASSWORD"] = $oCompteAd->getPwdtmp()->load();
            }

            $tab["COMPANY"] = $oCollaboration->getObjetRefidInstitution()->getMappingldap();
            $tab["PHYSICALDELIVERYOFFICENAME"] = $site;
            $tab["BUSINESSCATEGORY"] = $oCollaboration->getObjetRefidTypeCollaboration()->getMappingldap();
            $tab["EMPLOYEETYPE"] = $oIndividu->getObjetRefidCategorieProfessionnelle()->getMappingldap();
            $tab["DEPARTMENT"] = '';
            $tab["PREFERREDLANGUAGE"] = strtolower($oIndividu->getObjetRefidLangue()->getMappingldap());
            $tab["EMPLOYEENUMBER"] = $oIndividu->getNiss();
            //$tab["EXTENSIONATTRIBUTE2"]=''; //in out
            $tab["EXTENSIONATTRIBUTE1"] = '';

            //$tab['PAGER']=$oCollaboration->getPortable();
            $tab['DESCRIPTION'] = '';
            $tab["HOMEDIR"] = $oCollaboration->getObjetRefidInstitution()->getHomedir() . $oCompteAd->getUsername();
            $tab["HOMEDRIVE"] = $oCollaboration->getObjetRefidInstitution()->getHomedrive();
            $tab["EXTENSIONATTRIBUTE15"] = 'REFID-User'; //important
            if ($oCompteAd->getDatefin() != '') {
                $tab["ENABLEACCOUNTEXPIRES"] = 1;
            } else {
                $tab["ENABLEACCOUNTEXPIRES"] = 0;
            }

            $tab["ACCOUNTEXPIRES"] = $oCompteAd->getDatefin();
            //$tab["MAIL"]=strtoupper($oIndividu->getNomUsuel())."."
            $tab["CHANGEPASSWORDATLOGON"] = 1;
            $tab["ENABLED"] = 1;
            $tab["FLAGSYNCEXCHANGE"] = 0;
            if ($oCollaboration->getFlagdemandeemailinstitution() == 1) {
                $tab["ENABLEMAIL"] = 1;
                $tab['MAIL'] = '';
            } else {
                $tab["ENABLEMAIL"] = 0;
            }
            $tab["GROUPS"] = $groupe;
            $tab["DISTRIBUTIONLIST"] = $liste;
            $tab["ENV"] = $env;
            $tab["ORG"] = 'OSIRIS';
            $tab["USERCRE"] = $this->objetUserAcces->getLogin();
            $tab["DATECRE"] = trim(date('Y-m-d H:i:s'));
            $tab["USERUPD"] = $this->objetUserAcces->getLogin();
            $tab["DATEUPD"] = trim(date('Y-m-d H:i:s'));
            $tab["ACTIONTYPE"] = $action;
            $tab["MSGDB"] = 1;
            $tab["FLAGSYNCAD"] = 0;
            $tab["EXTENSIONATTRIBUTE11"] = '';
            $this->db->Exec_Query_SQL("select * from REFID_IOP_PROV_AD where SAMACCOUNTNAME='" . $oCompteAd->getUsername() . "'");
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            } else {
                if ($this->db->Fetch()) {
                    $this->db->Exec_Query('update', 'REFID_IOP_PROV_AD', $tab, "SAMACCOUNTNAME='" . $oCompteAd->getUsername() . "'");
                    if ($this->db->DataBase->Errno == 1) {
                        throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                    } else {
                        //  sleep(30);
                        $this->miseAjourDataRefidByPROV($oCollaboration->getIdindividufk());

                    }
                } else {
                    $this->db->Exec_Query('insert', 'REFID_IOP_PROV_AD', $tab);
                    if ($this->db->DataBase->Errno == 1) {
                        throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                    } else {
                        // sleep(30);
                        $this->miseAjourDataRefidByPROV($oCollaboration->getIdindividufk());
                    }
                }
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function provisionningTableUpdate($idindividu, $field)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            //on recupere les informations li�e a la collaboration�
            $tab["ORG"] = 'OSIRIS';
            $tab["USERUPD"] = $this->objetUserAcces->getLogin();
            $tab["DATEUPD"] = trim(date('Y-m-d H:i:s'));
            $tab["ACTIONTYPE"] = 'UPDATE';
            $tab["MSGDB"] = 1;
            $tab["ENV"] = 'DEV';
            $tab["FLAGSYNCAD"] = 0;
            $tab = array_merge($tab, $field);
            $this->db->Exec_QUERY("update", "REFID_IOP_PROV_AD", $tab, "SAMACCOUNTNAME in (
									select distinct  upper(username)
									FROM REFID_COMPTEAD rc JOIN REFID_COLLABORATION rc2 ON rc.IDCOLLABORATION_FK =rc2.IDCOLLABORATION
										 JOIN REFID_INDIVIDU ri ON rc2.IDINDIVIDU_FK =ri.IDINDIVIDU
									WHERE rc.invalide IS NULL AND rc2.invalide IS NULL AND  rc.flag_archive is null  and rc2.idIndividu_fk='" . $idindividu . "')");
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function provisionningTableUpdateByUsername($username, $field, $actiontype = 'UPDATE')
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            //on recupere les informations li�e a la collaboration�
            $tab["ORG"] = 'OSIRIS';
            $tab["USERUPD"] = $this->objetUserAcces->getLogin();
            $tab["DATEUPD"] = trim(date('Y-m-d H:i:s'));
            $tab["ACTIONTYPE"] = $actiontype;
            $tab["MSGDB"] = 1;
            $tab["ENV"] = 'DEV';
            $tab = array_merge($tab, $field);
            $this->db->Exec_QUERY("update", "REFID_IOP_PROV_AD", $tab, "SAMACCOUNTNAME ='" . $username . "'");
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function provisionningTableUpdateByCollaboration($idc, $field)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            //on recupere les informations li�e a la collaboration�
            $tab["ORG"] = 'OSIRIS';
            $tab["USERUPD"] = $this->objetUserAcces->getLogin();
            $tab["DATEUPD"] = trim(date('Y-m-d H:i:s'));
            $tab["ACTIONTYPE"] = 'UPDATE';
            $tab["FLAGSYNCAD"] = 0;
            $tab = array_merge($tab, $field);
            $tab["MSGDB"] = 1;
            $tab["ENV"] = 'DEV';
            $tab = array_merge($tab, $field);
            $this->db->Exec_QUERY("update", "REFID_IOP_PROV_AD", $tab, "SAMACCOUNTNAME in (
									select distinct upper(username)
									FROM REFID_COMPTEAD rc JOIN REFID_COLLABORATION rc2 ON rc.IDCOLLABORATION_FK =rc2.IDCOLLABORATION
										 JOIN REFID_INDIVIDU ri ON rc2.IDINDIVIDU_FK =ri.IDINDIVIDU
									WHERE rc.invalide IS NULL AND rc2.invalide IS NULL AND  rc.flag_archive is null  and rc2.idcollaboration='" . $idc . "')");
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function updateProvisionningTableByCollaboration($idcolloaboration, $env)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            //on recupere les informations li�e a la collaboration
            $obc = new RefidCompteAdDAO($this->objetUserAcces);
            $objetcolDAO = new RefidCollaborationDAO($this->objetUserAcces);
            $oCollaboration = $objetcolDAO->get($idcolloaboration);
            $objetIndDAO = new RefidIndividuDAO($this->objetUserAcces);
            $oIndividu = $objetIndDAO->getSignalitique($oCollaboration->getIdindividufk());
            $objetLocalisation = new RefidLocalisationDAO($this->objetUserAcces);
            $site = $objetLocalisation->getSiteProv($oCollaboration->getIdcollaboration());
            $objetAffectationDAO = new RefidAffectationDAO($this->objetUserAcces);
            $oAffectation = $objetAffectationDAO->getAffectationByCollaboration($oCollaboration->getIdcollaboration());
            $objetAffectationGroupeADDAO = new RefidAffectationGroupeADDAO($this->objetUserAcces);
            $groupe = $objetAffectationGroupeADDAO->getGroupeProv($oCollaboration->getIdcollaboration(), 'Security', $env);
            $liste = $objetAffectationGroupeADDAO->getGroupeProv($oCollaboration->getIdcollaboration(), 'Distribution', $env);
            $tabCompteAd = $this->listByCollaboration($oCollaboration->getIdcollaboration());
            $tab = array();
            foreach ($tabCompteAd as $index2 => $oCompteAd) {
                $tab["SAMACCOUNTNAME"] = $oCompteAd->getUsername();
                $tab["SN"] = strtoupper($oIndividu->getNomUsuel());
                $tab["GIVENNAME"] = ucfirst($oIndividu->getPrenomUsuel());
                if ($oCompteAd->getPwdtmp() != "") {
                    $tab["PASSWORD"] = $oCompteAd->getPwdtmp()->load();
                }

                $tab["COMPANY"] = $oCollaboration->getObjetRefidInstitution()->getMappingldap();
                $tab["PHYSICALDELIVERYOFFICENAME"] = $site;
                $tab["BUSINESSCATEGORY"] = $oCollaboration->getObjetRefidTypeCollaboration()->getMappingldap();
                $tab["EMPLOYEETYPE"] = $oIndividu->getObjetRefidCategorieProfessionnelle()->getMappingldap();
                $tab["DEPARTMENT"] = 'rh';
                $tab["PREFERREDLANGUAGE"] = strtolower($oIndividu->getObjetRefidLangue()->getMappingldap());
                $tab["EMPLOYEENUMBER"] = $oIndividu->getNiss();
                $tab["EXTENSIONATTRIBUTE2"] = ''; //in out
                $tab["EXTENSIONATTRIBUTE1"] = '';
                $tab["EXTENSIONATTRIBUTE11"] = $oIndividu->getInami();
                //$tab['PAGER']=$oCollaboration->getPortable();
                $tab['DESCRIPTION'] = '';
                $tab["HOMEDIR"] = $oCollaboration->getObjetRefidInstitution()->getHomedir() . $oCompteAd->getUsername();
                $tab["HOMEDRIVE"] = $oCollaboration->getObjetRefidInstitution()->getHomedrive();
                $tab["EXTENSIONATTRIBUTE15"] = 'REFID-User'; //important
                if ($oCompteAd->getDatefin() != '') {
                    $tab["ENABLEACCOUNTEXPIRES"] = 1;
                } else {
                    $tab["ENABLEACCOUNTEXPIRES"] = 0;
                }

                $tab["ACCOUNTEXPIRES"] = $oCompteAd->getDatefin();
                //$tab["MAIL"]=strtoupper($oIndividu->getNomUsuel())."."
                //$tab["CHANGEPASSWORDATLOGON"]=1;
                $tab["ENABLED"] = 1;
                $tab["FLAGSYNCEXCHANGE"] = 0;
                //if($oCollaboration->getFlagdemandeemailinstitution()==1){
                //$tab["ENABLEMAIL"]=1;
                //$tab['MAIL']='';
                //}else{ $tab["ENABLEMAIL"]=0;
                //}
                $tab["GROUPS"] = $groupe;
                $tab["DISTRIBUTIONLIST"] = $liste;
                $tab["ENV"] = $env;
                $tab["ORG"] = 'OSIRIS';
                $tab["USERUPD"] = $this->objetUserAcces->getLogin();
                $tab["DATEUPD"] = trim(date('Y-m-d H:i:s'));
                $tab["ACTIONTYPE"] = 'UPDATE';
                $tab["MSGDB"] = 1;
                $tab["FLAGSYNCAD"] = 0;
                $this->db->Exec_Query_SQL("select * from REFID_IOP_PROV_AD where SAMACCOUNTNAME='" . $oCompteAd->getUsername() . "'");
                if ($this->db->DataBase->Errno == 1) {
                    throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                } else {
                    if ($this->db->Fetch()) {
                        $this->db->Exec_Query('update', 'REFID_IOP_PROV_AD', $tab, "SAMACCOUNTNAME='" . $oCompteAd->getUsername() . "'");
                        if ($this->db->DataBase->Errno == 1) {
                            throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                        }
                    }
                }
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function updateProvisionningTableByID($idindividu, $env)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $objetIndDAO = new RefidIndividuDAO($this->objetUserAcces);
            $oIndividu = $objetIndDAO->getSignalitique($idindividu);
            //collaboration
            $objetcolDAO = new RefidCollaborationDAO($this->objetUserAcces);
            $taboCollaboration = $objetcolDAO->getByIdIndividu($idindividu, 1);
            //un individu peut avoir plusieurs collaboration
            foreach ($taboCollaboration as $index => $oCollaboration) {
                //localisation
                $objetLocalisation = new RefidLocalisationDAO($this->objetUserAcces);
                $site = "";
                $site = $objetLocalisation->getSiteProv($oCollaboration->getIdcollaboration());
                $objetAffectationDAO = new RefidAffectationDAO($this->objetUserAcces);
                $oAffectation = new RefidAffectation();
                $oAffectation = $objetAffectationDAO->getAffectationByCollaboration($oCollaboration->getIdcollaboration());
                $objetAffectationGroupeADDAO = new RefidAffectationGroupeADDAO($this->objetUserAcces);
                $groupe = "";
                $groupe = $objetAffectationGroupeADDAO->getGroupeProv($oCollaboration->getIdcollaboration(), 'Security', $env);
                $liste = "";
                $liste = $objetAffectationGroupeADDAO->getGroupeProv($oCollaboration->getIdcollaboration(), 'Distribution', $env);
                //pour la collaboration on recheche les diff?rents compte ad li?
                $tabCompteAd = $this->listByCollaboration($oCollaboration->getIdcollaboration());
                $tab = array();
                foreach ($tabCompteAd as $index2 => $oCompteAd) {
                    $tab["SAMACCOUNTNAME"] = $oCompteAd->getUsername();
                    $tab["SN"] = strtoupper($oIndividu->getNomUsuel());
                    $tab["GIVENNAME"] = ucfirst($oIndividu->getPrenomUsuel());
                    if ($oCompteAd->getPwdtmp() != "") {
                        $tab["PASSWORD"] = $oCompteAd->getPwdtmp()->load();
                    }

                    $tab["COMPANY"] = $oCollaboration->getObjetRefidInstitution()->getMappingldap();
                    $tab["PHYSICALDELIVERYOFFICENAME"] = $site;
                    $tab["BUSINESSCATEGORY"] = $oCollaboration->getObjetRefidTypeCollaboration()->getMappingldap();
                    $tab["EMPLOYEETYPE"] = $oIndividu->getObjetRefidCategorieProfessionnelle()->getMappingldap();
                    $tab["DEPARTMENT"] = '';
                    $tab["PREFERREDLANGUAGE"] = strtolower($oIndividu->getObjetRefidLangue()->getMappingldap());
                    $tab["EMPLOYEENUMBER"] = $oIndividu->getNiss();
                    //$tab["EXTENSIONATTRIBUTE2"]=''; //in out
                    $tab["EXTENSIONATTRIBUTE1"] = '';
                    $tab["EXTENSIONATTRIBUTE11"] = $oIndividu->getInami();
                    //$tab['PAGER']=$oCollaboration->getPortable();
                    $tab['DESCRIPTION'] = '';
                    $tab["HOMEDIR"] = $oCollaboration->getObjetRefidInstitution()->getHomedir() . $oCompteAd->getUsername();
                    $tab["HOMEDRIVE"] = $oCollaboration->getObjetRefidInstitution()->getHomedrive();
                    $tab["EXTENSIONATTRIBUTE15"] = 'REFID-User'; //important
                    if ($oCompteAd->getDatefin() != '') {
                        $tab["ENABLEACCOUNTEXPIRES"] = 1;
                    } else {
                        $tab["ENABLEACCOUNTEXPIRES"] = 0;
                    }

                    $tab["ACCOUNTEXPIRES"] = $oCompteAd->getDatefin();
                    //$tab["MAIL"]=strtoupper($oIndividu->getNomUsuel())."."
                    //$tab["CHANGEPASSWORDATLOGON"]=1;
                    $tab["ENABLED"] = 1;
                    $tab["FLAGSYNCEXCHANGE"] = 0;
                    //if($oCollaboration->getFlagdemandeemailinstitution()==1){
                    //$tab["ENABLEMAIL"]=1;
                    //$tab['MAIL']='';
                    //}else{ $tab["ENABLEMAIL"]=0;
                    //}
                    $tab["GROUPS"] = $groupe;
                    $tab["DISTRIBUTIONLIST"] = $liste;
                    $tab["ENV"] = $env;
                    $tab["ORG"] = 'OSIRIS';
                    $tab["USERUPD"] = $this->objetUserAcces->getLogin();
                    $tab["DATEUPD"] = trim(date('Y-m-d H:i:s'));
                    $tab["ACTIONTYPE"] = 'UPDATE';
                    $tab["MSGDB"] = 1;
                    $tab["FLAGSYNCAD"] = 0;

                    $this->db->Exec_Query_SQL("select * from REFID_IOP_PROV_AD where SAMACCOUNTNAME='" . $oCompteAd->getUsername() . "'");
                    if ($this->db->DataBase->Errno == 1) {
                        throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                    } else {
                        if ($this->db->Fetch()) {
                            $this->db->Exec_Query('update', 'REFID_IOP_PROV_AD', $tab, "SAMACCOUNTNAME='" . $oCompteAd->getUsername() . "'");
                            if ($this->db->DataBase->Errno == 1) {
                                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                            }
                        }
                    }
                }
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }
    public function passgen1($nbChar)
    {
        $chaine = "mnoTUzS5678kVvwxy9WXYZRNCDEFrslq41GtuaHIJKpOPQA23LcdefghiBMbj0";
        srand((double) microtime() * 1000000);
        $pass = '';
        for ($i = 0; $i < $nbChar; $i++) {
            $pass .= $chaine[rand() % strlen($chaine)];
        }
        return $pass;
    }
    public function resetepassword($id)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $o = new RefidComptead();
            $this->db->Exec_Query('select', "refid_comptead", RefidCompteadMap::getTabChamps(), " IDCOMPTEAD =" . $id);
            if ($this->db->DataBase->Errno == 0) {
                if ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->DataBase->Get_Record());
                    $o = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                    //creation du mot de passe provisoire
                    $o = $this->generatePassword($o);
                    if ($this->getError() == 1) {
                        $this->db->Exec_Query_SQL("update refid_individu set statutaction=5 where idindividu=" . $o->getIdindividufk());
                        throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']: add pwd comptead', 2);
                    } //Tool::debug($data['refid_comptead_pwdtmp']->load());
                }
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $o;
    }
    public function getLastAccount($idIndividu)
    {
        RefidGestionException::toException();
        try {
            $o = null;
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query('select', $this->table . " refid_comptead  left JOIN refid_individu refid_individu ON refid_comptead.idindividu_fk = refid_individu.idindividu left JOIN refid_collaboration refid_collaboration ON refid_comptead.idcollaboration_fk = refid_collaboration.idcollaboration", array_merge(RefidCompteadMap::getTabChamps(), RefidIndividuMap::getTabChamps(), RefidCollaborationMap::getTabChamps()), "idcomptead= (select max(idcomptead) from refid_comptead where statut='NEW' and idIndividu_fk='" . $idIndividu . "')");
            if ($this->db->DataBase->Errno == 0) {
                if ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->DataBase->Get_Record());
                    $o = new RefidComptead();
                    $o = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                    $oRefidIndividu = new RefidIndividu();
                    $oRefidIndividu = ConnectionDB::buildObject($oRefidIndividu, RefidIndividuMap::getTabMapping(), $data);
                    $o->setObjetRefidIndividu($oRefidIndividu);
                    $oRefidCollaboration = new RefidCollaboration();
                    $oRefidCollaboration = ConnectionDB::buildObject($oRefidCollaboration, RefidCollaborationMap::getTabMapping(), $data);
                    $o->setObjetRefidCollaboration($oRefidCollaboration);
                    //Tool::debug($o);
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $o;
    }
    public function miseAjourDataRefidByPROV($idindividu = '')
    {$where = '';
        if ($idindividu = '') {
            $where = " and rc2.idindividu_fk=" . $idindividu;
        }

        $sql = "select rc2.idcollaboration , ripa.MAIL ,ripa.OBJECTGUID ,ripa.OBJECTSID,rc.username FROM REFID_COLLABORATION rc2
		JOIN REFID_COMPTEAD rc ON rc2.IDCOLLABORATION = rc.IDCOLLABORATION_FK JOIN REFID_IOP_PROV_AD ripa ON rc.USERNAME =ripa.SAMACCOUNTNAME
		 WHERE rc2.FLAG_DEMANDE_EMAIL_INSTITUTION =1 AND rc2.EMAIL_INSTITUTION  IS NULL and ripa.FLAGSYNCAD=1 and ripa.FLAGSYNCEXCHANGE=1" . $where;
        RefidGestionException::toException();
        try {
            $o = null;
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db2 = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query_SQL($sql);
            if ($this->db->DataBase->Errno == 0) {
                if ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->DataBase->Get_Record());
                    //mise ajour compte ad
                    $this->db2->Exec_QUery("update", "refid_comptead", array("guid" => $data['objectguid'], "sid" => $data['objectsid']), "username='" . $data['username'] . "'");
                    if ($this->db2->DataBase->Errno == 0) {
                        //mise ajour collaboration mail
                        $this->db2->Exec_QUery("update", "refid_collaboration", array("email_institution" => $data['mail']), "idcollaboration=" . $data['idcollaboration']);
                        if ($this->db2->DataBase->Errno == 1) {
                            throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                        }

                    } else {
                        throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                    }

                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
    }
    public function updateprovisionningTable($oCompteAd, $env)
    {
        RefidGestionException::toException();
        try {
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            //on recupere les informations li�e a la collaboration
            $obc = new RefidCompteAdDAO($this->objetUserAcces);
            $objetcolDAO = new RefidCollaborationDAO($this->objetUserAcces);
            $oCollaboration = $objetcolDAO->get($oCompteAd->getIdcollaborationfk());
            $objetIndDAO = new RefidIndividuDAO($this->objetUserAcces);
            $oIndividu = $objetIndDAO->getSignalitique($oCollaboration->getIdindividufk());
            $objetLocalisation = new RefidLocalisationDAO($this->objetUserAcces);
            $site = $objetLocalisation->getSiteProv($oCompteAd->getIdcollaborationfk());
            $objetAffectationDAO = new RefidAffectationDAO($this->objetUserAcces);
            $oAffectation = $objetAffectationDAO->getAffectationByCollaboration($oCollaboration->getIdcollaboration());
            $objetAffectationGroupeADDAO = new RefidAffectationGroupeADDAO($this->objetUserAcces);
            $groupe = $objetAffectationGroupeADDAO->getGroupeProv($oCollaboration->getIdcollaboration(), 'Security', $env);
            $liste = $objetAffectationGroupeADDAO->getGroupeProv($oCollaboration->getIdcollaboration(), 'Distribution', $env);
            //$tab["TELEPHONENUMBER"]=$oAffectation->telephone_fixe;
            $tab["SAMACCOUNTNAME"] = $oCompteAd->getUsername();
            $tab["SN"] = strtoupper($oIndividu->getNomUsuel());
            $tab["GIVENNAME"] = ucfirst($oIndividu->getPrenomUsuel());
            if ($oCompteAd->getPwdtmp() != "") {
                $tab["PASSWORD"] = $oCompteAd->getPwdtmp()->load();
            }

            $tab["COMPANY"] = $oCollaboration->getObjetRefidInstitution()->getMappingldap();
            $tab["PHYSICALDELIVERYOFFICENAME"] = $site;
            $tab["BUSINESSCATEGORY"] = $oCollaboration->getObjetRefidTypeCollaboration()->getMappingldap();
            $tab["EMPLOYEETYPE"] = $oIndividu->getObjetRefidCategorieProfessionnelle()->getMappingldap();
            $tab["DEPARTMENT"] = 'rh';
            $tab["PREFERREDLANGUAGE"] = strtolower($oIndividu->getObjetRefidLangue()->getMappingldap());
            $tab["EMPLOYEENUMBER"] = $oIndividu->getNiss();
            $tab["EXTENSIONATTRIBUTE2"] = ''; //in out
            $tab["EXTENSIONATTRIBUTE1"] = '';
            $tab["EXTENSIONATTRIBUTE11"] = $oIndividu->getInami();
            //$tab['PAGER']=$oCollaboration->getPortable();
            $tab['DESCRIPTION'] = '';
            $tab["HOMEDIR"] = $oCollaboration->getObjetRefidInstitution()->getHomedir() . $oCompteAd->getUsername();
            $tab["HOMEDRIVE"] = $oCollaboration->getObjetRefidInstitution()->getHomedrive();
            $tab["EXTENSIONATTRIBUTE15"] = 'REFID-User'; //important
            if ($oCompteAd->getDatefin() != '') {
                $tab["ENABLEACCOUNTEXPIRES"] = 1;
            } else {
                $tab["ENABLEACCOUNTEXPIRES"] = 0;
            }

            $tab["ACCOUNTEXPIRES"] = $oCompteAd->getDatefin();
            //$tab["MAIL"]=strtoupper($oIndividu->getNomUsuel())."."
            //$tab["CHANGEPASSWORDATLOGON"]=1;
            $tab["ENABLED"] = 1;
            $tab["FLAGSYNCEXCHANGE"] = 0;
            //if($oCollaboration->getFlagdemandeemailinstitution()==1){
            //$tab["ENABLEMAIL"]=1;
            //$tab['MAIL']='';
            //}else{ $tab["ENABLEMAIL"]=0;
            //}
            $tab["GROUPS"] = $groupe;
            $tab["DISTRIBUTIONLIST"] = $liste;
            $tab["ENV"] = $env;
            $tab["ORG"] = 'OSIRIS';
            $tab["USERUPD"] = $this->objetUserAcces->getLogin();
            $tab["DATEUPD"] = trim(date('Y-m-d H:i:s'));
            $tab["ACTIONTYPE"] = 'UPDATE';
            $tab["MSGDB"] = 1;
            $tab["FLAGSYNCAD"] = 0;
            $this->db->Exec_Query_SQL("select * from REFID_IOP_PROV_AD where SAMACCOUNTNAME='" . $oCompteAd->getUsername() . "'");
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            } else {
                if ($this->db->Fetch()) {
                    $this->db->Exec_Query('update', 'REFID_IOP_PROV_AD', $tab, "SAMACCOUNTNAME='" . $oCompteAd->getUsername() . "'");
                    if ($this->db->DataBase->Errno == 1) {
                        throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
                    }
                }
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
    }

    public function getCompteByIndividuAndInstitutionWithFlagCreationTrue($idindividu, $idinstitution)
    {

        RefidGestionException::toException();
        try {
            $tabobjet = array();
            $this->db = ConnectionDB::getConnection($this->typedb, $this->DBLA);
            $this->db->Exec_Query('select', " refid_collaboration refid_collaboration
								 JOIN refid_comptead refid_comptead
								  on refid_collaboration.idcollaboration = refid_comptead.idcollaboration_fk "
                , array_merge(RefidCompteadMap::getTabChamps(), RefidCollaborationMap::getTabChamps()),
                "(refid_collaboration.IDINDIVIDU_FK=" . $idindividu . "  AND refid_collaboration.IDINSTITUTION_FK=" . $idinstitution .
                " AND refid_collaboration.INVALIDE IS NULL AND refid_collaboration.FLAG_DEMANDE_EMAIL_INSTITUTION=1)
									 AND (refid_comptead.INVALIDE IS NULL)");
            if ($this->db->DataBase->Errno == 0) {
                while ($this->db->Fetch()) {
                    $data = array_change_key_case($this->db->DataBase->Get_Record());
                    $o = new RefidComptead();
                    $o = ConnectionDB::buildObject($o, RefidCompteadMap::getTabMapping(), $data);
                    $oRefidCollaboration = new RefidCollaboration();
                    $oRefidCollaboration = ConnectionDB::buildObject($oRefidCollaboration, RefidCollaborationMap::getTabMapping(), $data);
                    $o->setObjetRefidCollaboration($oRefidCollaboration);
                    $tab[$o->getIdcomptead()] = $o;
                }
            } else {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:', 2);
            }

        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $tab;
    }
	
	function injectRegleAd(){
	
		$this->error = 0;
        $this->txterror = '';
        RefidGestionException::toException();
        try {    
			$groupe=array();
			
			 $this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA); 
		
		//1 lecture du fichier groupes qui contient les distinguishdname  provevannt du document d'analyse
		// on met en formet et on regarde si on trouve une conresponse dans la table ref_iop_rad
			if (($handle = fopen("d:/web/intranet/refidv1/classes/DAO/groupes.csv", "r")) !== FALSE) {
			while (($data = fgetcsv($handle, 1000, ";")) !== FALSE) {
				$tmp=array();
				$tmp=explode(";",$data[0]);
				//on r�cupere les �l�ments ligne par ligne et on cr�e un tableau
				$tmp=Tool::decode_data($tmp);
				$infogroupe=strtoupper($tmp[0]);
				$infogroupe=str_replace("'","''",trim($infogroupe));
				$infogroupe=str_replace(" ","",trim($infogroupe));
				//echo $infogroupe."<br/>";
				//$datap['libelle']=trim($tmp[0]);
				//on regarde dans la table de refad de christian si on retrouve la correspondance pour r�cuperer l'id
				 $this->db->Exec_Query_SQL("select distinct upper(DISTINGUISHEDNAME),id from refid_iop_refadgroups where upper(replace(DISTINGUISHEDNAME,' ',''))='".$infogroupe."'");
				while($this->db->Fetch()) $groupe[$infogroupe]=$this->db->Get_Field("id");
			}//while
		}						
		fclose($handle);
		

	    /*	$hos=array();
		//on recup�re la  liste des institions d�finie dans la db refid
		$this->db->Exec_Query_SQL("select upper(lib_fr) as lib,idinstitution from refid_institution");
	    while($this->db->Fetch()) $hos[$this->db->Get_Field("lib")]=$this->db->Get_Field("idinstitution");
		
		// on recup�re les type d'emmploy�s dans la db refid
		$type=array();
		$this->db->Exec_Query_SQL("select upper(lib_fr) as lib,id from refid_employee_type");
		while($this->db->Fetch()) $type[$this->db->Get_Field("lib")]=$this->db->Get_Field("id");

		//on recup�re l'ensemble des sites , un site est toujours associ� � une institution
		$site=array();
		$this->db->Exec_Query_SQL("select idsite, upper(lib_fr) as lib,idinstitution_fk from refid_site");
		while($this->db->Fetch()) $site[$this->db->Get_Field("idinstitution_fk")][$this->db->Get_Field("lib")]=$this->db->Get_Field("idsite");
			*/	 

		/* #on recupere le fichier qui contient les cl�s li� a un groupes
			ensuite on met chaques elements dans une variable que l'on met en majuscule et on retire les blancs
			*/
	    $hos = array(
        "CHU-BRUGMANN"=> "CHU-BRUGMANN", "HUDERF"=> "HUDERF","BRUSTP"=> "BRUSTP"  );

        $site =array (
            "CHU-BRUGMANN"=>array("HORTA"=> "HORTA","BRIEN"=> "BRIEN","ASTRID"=> "ASTRID"),
            "HUDERF"=>array("HORTA"=> "HORTA"),
            "BRUSTP"=>array("HORTA"=> "HORTA","BRIEN"=> "BRIEN","ASTRID"=> "ASTRID")
            );

        $type =array (
        "ADMINISTRATIF"=> "ADMINISTRATIF",
        "MEDICAL"=> "MEDICAL",
        "NURSING"=> "NURSING",
        "PARAMEDICAL"=> "PARAMEDICAL",
        "TECHNIQUE"=> "TECHNIQUE",
        "OUVRIER"=> "OUVRIER",
        "OTHER"=> "OTHER",
        "UNKNOWN"=> "UNKNOWN");
		$this->db->Exec_Query_SQL("delete  from refid_iop_rule_attribution_with_key");

		$i=1;
		 if (($handle = fopen("d:/web/intranet/refidv1/classes/DAO/rules.csv", "r")) !== FALSE) {
			while (($data = fgets($handle)) !== FALSE) {
				$tmp=array();
				$tmp=explode(";",$data);
			
				$keyhopt=strtoupper($tmp[0]); //institution
				$keysite=strtoupper($tmp[1]); //site
				$keytype=strtoupper($tmp[2]);//employeetype
				$distinguishdname=strtoupper($tmp[4]); //distinguishdname
				$distinguishdname=str_replace("'","''",trim($distinguishdname));
				$distinguishdname=str_replace(" ","",trim($distinguishdname));				
					echo $keyhopt." ".$keysite." ".$keytype." ".$distinguishdname."<br/>";
				//on stocke la regl�e et le groupe associ� dans la table apr�s avoir r�cup�rer les identifiants li�s 
				// exemple Chu-BRUGMANN ID 32 dans la table refid_institutionn
				$this->db->Exec_Query("insert","refid_iop_rule_attribution_with_key",array("idrule"=>$i,
																						"institution"=>$hos[$keyhopt],
																						"site"=>$site[$hos[$keyhopt]][$keysite],"employeetype"=>$type[$keytype],
																						"id_groupe"=>$groupe[$distinguishdname]));
					$i++;
			}//while*/
		}						
		fclose($handle);
			
       } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::Stop();
		

	}

	function testRegleAd(){
	
		$this->error = 0;
        $this->txterror = '';
        RefidGestionException::toException();
        try {    
			$groupe=array();
			   $hos = array(
        "CHU-BRUGMANN"=> "CHU-BRUGMANN",
        "HUDERF"=> "HUDERF",
        "BRUSTP"=> "BRUSTP"  );

        $site =array (
            "HORTA"=> "HORTA",
            "BRIEN"=> "BRIEN",
            "ASTRID"=> "ASTRID"   );

        $type =array (
            "ADMINISTRATIF"=> "ADMINISTRATIF",
            "MEDICAL"=> "MEDICAL",
            "NURSING"=> "NURSING",
            "PARAMEDICAL"=> "PARAMEDICAL",
            "TECHNIQUE"=> "TECHNIQUE",
            "OUVRIER"=> "OUVRIER",
            "OTHER"=> "OTHER",
            "UNKNOWN"=> "UNKNOWN");
        
                $this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA); 
                $this->db2=ConnectionDB::getConnection($this->typedb,$this->DBLA); 
                //on recupere les records dans la table de provisionning init
                $this->db->Exec_Query_SQL("select upper(company) hos,upper(EMPLOYEETYPE) emptype,upper(PHYSICALDELIVERYOFFICENAME) site, samaccountname,upper(groups) as g,upper(distributionlist)
                                                    as l from refid_iop_provinit_ad where company='Huderf'");
                while($this->db->Fetch()){
                    $samaccountname=$this->db->Get_Field("samaccountname");
                    $hospi=$this->db->Get_Field("hos"); //institution
                    $site=$this->db->Get_Field("site"); //site
                    $type=$this->db->Get_Field("emptype"); //employtype
                    $cle=$hospi.$site.$type; //formation de la cl�
                    
                    $groups=explode(";",$this->db->Get_Field("g")); //group stocker dans la table prov
                    $list=explode(";",$this->db->Get_Field("l")); //liste de distribution
                    
                    //on v�rifie si la cl� se trouve bien dans la table des regles pour r�cuperer les groupes associ�s
                    $this->db2->Exec_Query_SQL(" SELECT  ri.LIB_FR ,rs.LIB_FR , upper(ri.LIB_FR|| rs.LIB_FR || ret.LIB_FR) cle ,rir.DISTINGUISHEDNAME ,rir.GROUPCATEGORY 
                                        FROM    REFID_IOP_RULE_ATTRIBUTION rira LEFT JOIN REFID_INSTITUTION ri ON rira.IDINSTITUTION_FK =ri.IDINSTITUTION 
                                                LEFT JOIN REFID_SITE rs ON  rira.IDSITE_FK=rs.IDSITE  AND rs.IDINSTITUTION_FK =ri.IDINSTITUTION 
                                                LEFT JOIN REFID_EMPLOYEE_TYPE ret ON rira.ID_EMPLOYEETYPE =ret.ID 
                                                LEFT JOIN REFID_IOP_REFADGROUPS rir ON rira.ID_REFAD  = rir.ID 
                                                where  upper(ri.LIB_FR|| rs.LIB_FR || ret.LIB_FR)='".$cle."' and rir.DISTINGUISHEDNAME is not null");
                                            
                    echo "<h1>Samaccountname ".$samaccountname."<h1>";
                    echo "<h2>droit</h2>";
                    while($this->db2->Fetch()){
                        echo $this->db2->Get_Field("cle")." ==>". $this->db2->Get_Field("DISTINGUISHEDNAME").' Type:'.$this->db2->Get_Field("GROUPCATEGORY")."<br/>";	
                
                    }
                    echo "<h3>groups</h3>	 ";
                    Tool::debug($groups);

                    echo "<h3>liste></h3>	 UX/UI du Module de base (Tous les users) d�finie";
                    Tool::debug($list);
            }
            
            //1 lecture du fichier groupes qui contient les distinguishdname  provevannt du document d'analyse
            // on met en formet et on regarde si on trouve une conresponse dans la table ref_iop_rad
                if (($handle = fopen("d:/web/intranet/refidv1/classes/DAO/groupes.csv", "r")) !== FALSE) {
                while (($data = fgetcsv($handle, 1000, ";")) !== FALSE) {
                    $tmp=array();
                    $tmp=explode(";",$data[0]);
                    //on r�cupere les �l�ments ligne par ligne et on cr�e un tableau
                    $tmp=Tool::decode_data($tmp);
                    $infogroupe=strtoupper($tmp[0]);
                    $infogroupe=str_replace("'","''",trim($infogroupe));
                    $infogroupe=str_replace(" ","",trim($infogroupe));
                    //$datap['libelle']=trim($tmp[0]);
                    //on regarde dans la table de refad de christian si on retrouve la correspondance pour r�cuperer l'id
                    $this->db->Exec_Query_SQL("select upper(DISTINGUISHEDNAME),id from refid_iop_refadgroups where upper(replace(DISTINGUISHEDNAME,' ',''))='".$infogroupe."'");
                    if($this->db->Fetch()) $groupe[$droit]=$this->db->Get_Field("id");
                }//while
            }						
            fclose($handle);
            
            
            /*$hos=array();
            //on recup�re la  liste des institions d�finie dans la db refid
            $this->db->Exec_Query_SQL("select upper(lib_fr) as lib,idinstitution from refid_institution");
            while($this->db->Fetch()) $hos[$this->db->Get_Field("lib")]=$this->db->Get_Field("idinstitution");
            
            // on recup�re les type d'emmploy�s dans la db refid
            $type=array();
            $this->db->Exec_Query_SQL("select upper(lib_fr) as lib,id from refid_employee_type");
            while($this->db->Fetch()) $type[$this->db->Get_Field("lib")]=$this->db->Get_Field("id");

            //on recup�re l'ensemble des sites , un site est toujours associ� � une institution
            $site=array();
            $this->db->Exec_Query_SQL("select idsite, upper(lib_fr) as lib,idinstitution_fk from refid_site");
            while($this->db->Fetch()) $site[$this->db->Get_Field("idinstitution_fk")][$this->db->Get_Field("lib")]=$this->db->Get_Field("idsite");
                    

            /* #on recupere le fichier qui contient les cl�s li� a un groupes
                ensuite on met chaques elements dans une variable que l'on met en majuscule et on retire les blancs
                */
                
                    $hos = array(
            "CHU-BRUGMANN"=> "CHU-BRUGMANN",
            "HUDERF"=> "HUDERF",
            "BRUSTP"=> "BRUSTP"  );

        $site =array (
            "HORTA"=> "HORTA",
            "BRIEN"=> "BRIEN",
            "ASTRID"=> "ASTRID"   );

        $type =array (
        "ADMINISTRATIF"=> "ADMINISTRATIF",
        "MEDICAL"=> "MEDICAL",
        "NURSING"=> "NURSING",
        "PARAMEDICAL"=> "PARAMEDICAL",
        "TECHNIQUE"=> "TECHNIQUE",
        "OUVRIER"=> "OUVRIER",
        "OTHER"=> "OTHER",
        "UNKNOWN"=> "UNKNOWN");
	
		$i=1;	
		echo "<h1>d".$keyhopt." ".$keysite." ".$keytype." ".$distinguishdname."</h1><br/>";
		 if (($handle = fopen("d:/web/intranet/refidv1/classes/DAO/rules.csv", "r")) !== FALSE) {
			while (($data = fgets($handle)) !== FALSE) {
				$tmp=array();
				$tmp=explode(";",$data);
				$keyhopt=strtoupper($tmp[0]); //institution
				$keysite=strtoupper($tmp[1]); //site
				$keytype=strtoupper($tmp[2]);//employeetype
				$distinguishdname=strtoupper($tmp[4]); //distinguishdname
				$distinguishdname=str_replace("'","''",trim($distinguishdname));
				$distinguishdname=str_replace(" ","",trim($distinguishdname));				
				
				//on stocke la regl�e et le groupe associ� dans la table apr�s avoir r�cup�rer les identifiants li�s 
				// exemple Chu-BRUGMANN ID 32 dans la table refid_institutionn
				$this->db->Exec_Query("insert","refid_iop_rule_attribution",array("idrule"=>$i,
																						"idinstitution_fk"=>$hos[$keyhopt],
																						"idsite_fk"=>$site[$hos[$keyhopt]][$keysite],"id_employeetype"=>$type[$keytype],
																						"id_refad"=>$groupe[$distinguishdname]));
					$i++;
			}//while*/
		}						
		fclose($handle);
			
       } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::Stop();
		

	}

}
