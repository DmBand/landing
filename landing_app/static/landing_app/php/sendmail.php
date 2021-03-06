<?php
    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;

    require 'phpmailer/src/Exception.php';
    require 'phpmailer/src/PHPMailer.php';

    $mail = new PHPMailer(true);
    $mail->CharSet = 'UTF-8';
    $mail->setLanguage('ru', 'phpmailer/language/');
    $mail->IsHTML(true);

    // От кого
    $mail->setFrom('d.bandysik@gmail.com', 'Лендинг');
    // Кому
    $mail->addAddress('d.bandysik@gmail.com');
    // Тема письма
    $mail->Subject = 'Запрос на обратный звонок';

    // Письмо
    $body = '<h1>Поступил запрос на обратный звонок</h1>';

    if (trim(!empty($_POST['name']))){
        $body.='<p><strong>Имя:</strong> '.$_POST['name'].'</p>';
    }

    if (trim(!empty($_POST['tel']))){
        $body.='<p><strong>Телефон:</strong> '.$_POST['tel'].'</p>';
    }
    
    if (trim(!empty($_POST['message']))){
        $body.='<p><strong>Сообщение:</strong> '.$_POST['message'].'</p>';
    }

    $mail->Body = $body;

    // Отправляем
    if (!$mail->send()) {
        $message = 'Ошибка';
    } else {
        $message = 'Данные успешно отправлены!';
    }

    $response = ['message' => $message];

    header('Content-type: application/json');
    echo json_encode($response);
?>
