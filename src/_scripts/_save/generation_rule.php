<?php @header('Content-type: text/html; charset=iso-8859-1');
include_once('../initialisation.php');
$debug=1;
$objetDAO = new RefidCompteAdDAO($userAuthentification);
$objetDAO->injectRegleAd();
//$objetDAO->testRegleAd();

?>
