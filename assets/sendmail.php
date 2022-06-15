<?php
    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\PHPMailer;

    require 'phpmailer/src/Exception.php';
    require 'phpmailer/src/PHPMailer.php';

    $mail = new PHPMailer(true);
    $mail->CharSet = 'utf-8';
    $mail->setLanguage('ru', 'phpmailer/language');
    $mail->IsHTML(true);

    // От кого
    $mail->setForm('d.bandysik@yandex.by', 'Лендинг');
    // Кому
    $mail->addAddress('d.bandysik@gmail.com');
    // Тема письма
    $mail->Subject = 'Запрос на обратный звонок';

    // Письмо
    $body = '<h1>Поступил запрос на обратный звонок</h1>'

    if(trim(!empty($_POST['name']))){
        $body.='<p><strong>Имя:</strong> '.$_POST['name'].'</p>';
    }