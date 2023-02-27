<?php require_once($BASEDIR.'classes/ConnectionDB.class.php');
require_once($BASEDIR.'classes/Traduction.class.php');
require_once($BASEDIR.'classes/RefidGestionException.php');
require_once($BASEDIR.'classes/Modeles/RefidFonction.class.php');
require_once($BASEDIR.'classes/Map/RefidFonctionMap.class.php');
if (class_exists('RefidFonctionDAO'))  return true;
 class RefidFonctionDAO {
	private $table ='REFID_FONCTION' ;
	 private $db;
	 private $typedb='oracle';
	 private $prefix_l = '_FR';
	 private $DBLA = 'informatique';
	 private $langueUser = 'FR';
	 private $traduction;
	 private $error;
	 private $txterror;
	 private $nhop = 26;
	  private $objetUserAcces;
	 public function __construct($objUserAcces){
	$this->objetUserAcces=$objUserAcces;	 
	$this->langueUser = $this->objetUserAcces->getLangueUser();
	if ($this->langueUser == '') $this->langueUser = 'FR';
	$this->traduction = new Traduction($this->langueUser);
	if ($this->langueUser == 'NL') $this->prefix_l = '_NL';
	$this->nhop=$this->objetUserAcces->getViewHopital();	
	}
	public function getError(){
	 return $this->error;
	}
	public function getTxtError(){
	 return $this->txterror;
	}
	public function getChamps(){
	 return $this->champs;
	}
	public function getTable(){
	 return $this->table;
	}
	public function add($o){
	RefidGestionException::toException();
	try {
	$this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA);
	$this->db->Exec_Query('insert',$this->table,ConnectionDB::builMapRequest($o,RefidFonctionMap::getTabMapping()));
	if ($this->db->DataBase->Errno == 1) {
			throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:',2);
	}
		} catch (Exception $e) {
	$this->error = 1;
	$this->txterror = $e->getMessage();
	}
	RefidGestionException::stop();
	}
	public function update($o){
	RefidGestionException::toException();
	try {
	$this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA);
	$this->db->Exec_Query('update',$this->table,ConnectionDB::builMapRequest($o,RefidFonctionMap::getTabMapping()),"idfonction='".$o->getIdfonction()."'");
	if ($this->db->DataBase->Errno == 1) {
		throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:',2);
	}
		} catch (Exception $e) {
	$this->error = 1;
	$this->txterror = $e->getMessage();
	}
	RefidGestionException::stop();
	}
	public function get($idfonction){
	RefidGestionException::toException();
	try {
	$o=null;
	$this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA);
	$this->db->Exec_Query('select',$this->table. " refid_fonction left join refid_categorie_professionnelle 
	refid_categorie_professionnelle on refid_fonction.idcategorieprof_fk =refid_categorie_professionnelle.idcatprof",array_merge(RefidCategorieProfessionnelleMap::getTabChamps(),RefidFonctionMap::getTabChamps()),"idfonction='".$idfonction."'");
	if ($this->db->DataBase->Errno == 0) {
		if ($this->db->Fetch()) {
			$data = array_change_key_case($this->db->DataBase->Get_Record());
			$o=new RefidFonction();
			$ocategorie=new RefidCategorieProfessionnelle();
			$ocategorie=ConnectionDB::buildObject($ocategorie,RefidCategorieProfessionnelleMap::getTabMapping(),$data);
			$o=ConnectionDB::buildObject($o,RefidFonctionMap::getTabMapping(),$data);
			$o->setObjetRefidCategorieProfessionelle($ocategorie);
			
			}
	}else throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:',2);
	
		} catch (Exception $e) {
	$this->error = 1;
	$this->txterror = $e->getMessage();
	}
	RefidGestionException::stop();
	return $o;
	}
	function countlisting($params = array())
    { 
        $nb = 0;
        RefidGestionException::toException();
        try {
				
             
			  $where = '';
                  if ($params['rechercher'] != '') {
			   $params=Tool::doubleQuoteSQL($params);	
                if (is_numeric($params['rechercher'])) {
                    $where = " where ( refid_fonction.idfonction=".$params['rechercher'].")";
                }  else {
                    $where = " where ( upper(refid_fonction.lib_fr) like upper('%".$params['rechercher']."%') 
					or upper(refid_fonction.lib_nl) like upper('%".$params['rechercher']."%')
					)";
                }
            } //count
			$this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA);
            $this->db->Exec_Query_SQL(" select count(*) as nb
            from (
            select ROW_NUMBER() OVER (ORDER BY idfonction asc) R, idfonction
            from REFID_FONCTION refid_fonction  
            " . $where . ")");
            if ($this->db->DataBase->Errno == 0) {
                if ($this->db->Fetch()) {
                    $nb = $this->db->Get_Field('nb');
                }
            }else throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:',2);
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::stop();
        return $nb;
    }
	 function listing($page = 1, $pas = 10, $params =array())
    { //OK

        $tab = array();
        RefidGestionException::toException();
        try {
            if ($page > 1) {
                $avant = $page - 1;
                $avant = $avant * $pas;
            } else $avant = 0;
            $apres = $page * $pas;
     
			  $where = '';
                  if ($params['rechercher'] != '') {
			   $params=Tool::doubleQuoteSQL($params);	
                if (is_numeric($params['rechercher'])) {
                    $where = " where ( refid_fonction.idfonction=".$params['rechercher'].")";
                }  else {
                    $where = " where ( upper(refid_fonction.lib_fr) like upper('%".$params['rechercher']."%') 
					or upper(refid_fonction.lib_nl) like upper('%".$params['rechercher']."%')
					)";
                }
            } //count
			$dtmp=array_merge(RefidFonctionMap::getTabChamps(),RefidCategorieProfessionnelleMap::getTabChamps());
			$datamap=implode(",",array_keys($dtmp));
			unset($dtmp);
		$this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA);
		$this->db->Exec_Query_SQL("
            select *
            from (
                        select ROW_NUMBER() OVER (ORDER BY idfonction)  R,".$datamap." 
                         from ".$this->table." refid_fonction  left join refid_categorie_professionnelle 
								 refid_categorie_professionnelle on refid_fonction.idcategorieprof_fk =refid_categorie_professionnelle.idcatprof
						 " . $where . "
                ) WHERE R >=" . $avant . " and R<=" . $apres);
			if ($this->db->DataBase->Errno == 0) {
				while ($this->db->Fetch()) {
					$data = array_change_key_case($this->db->Get_Record());
					$o=new RefidFonction();
					$ocategorie=new RefidCategorieProfessionnelle();
					$ocategorie=ConnectionDB::buildObject($ocategorie,RefidCategorieProfessionnelleMap::getTabMapping(),$data);			
					$o->setObjetRefidCategorieProfessionelle($ocategorie);
					$cle=strtolower($this->table.'_idfonction');
					$tab[$data[$cle]] = ConnectionDB::buildObject($o,RefidFonctionMap::getTabMapping(),$data);
				}
			} else throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:',2);
		} catch (Exception $e) {
		$this->error = 1;
		$this->txterror = $e->getMessage();
		}
		RefidGestionException::stop();
		return $tab;
		}
		 function listeOption()
    { //OK

        $tab = array();
        RefidGestionException::toException();
        try {
           			
		$this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA);
		$this->db->Exec_Query("select",$this->table,RefidFonctionMap::getTabChamps());          
			if ($this->db->DataBase->Errno == 0) {
				while ($this->db->Fetch()) {
					$data = array_change_key_case($this->db->Get_Record());
					$o=new RefidFonction();
					
					$cle=strtolower($this->table.'_idfonction');
					$tab[$data[$cle]] = ConnectionDB::buildObject($o,RefidFonctionMap::getTabMapping(),$data);
				}
			} else throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']:',2);
		} catch (Exception $e) {
		$this->error = 1;
		$this->txterror = $e->getMessage();
		}
		RefidGestionException::stop();
		return $tab;
		}
	  function active($idfonction, $actif = 1,$login='')
    {
        $this->error = 0;
        $this->txterror = '';
        RefidGestionException::toException();
        try {
            $this->db=ConnectionDB::getConnection($this->typedb,$this->DBLA);           
            if ($actif == 1)
                $this->db->Exec_Query_SQL("update ".$this->table." set invalideur='".$login."',invalide=TO_DATE('" . trim(date('d/m/Y H:i:s')) . "','DD/MM/YYYYHH24:MI:SS') where idfonction='".$idfonction."'");
            else
                $this->db->Exec_Query_SQL("update ".$this->table." set invalide='',invalideur='' where idfonction='".$idfonction."'");
			
            if ($this->db->DataBase->Errno == 1) {
                throw new RefidGestionException('ERROR [' . __CLASS__ . '::' . __FUNCTION__ . ']' . $this->traduction->getError("err2"), 2);
            }
        } catch (Exception $e) {
            $this->error = 1;
            $this->txterror = $e->getMessage();
        }
        RefidGestionException::Stop();
    }
	
}
 ?>