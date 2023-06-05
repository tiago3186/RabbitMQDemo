## RabbitMQDemo
Uma demonstração de uso do RabbitMQ com Django e Flask em uma pagina HTML.

### O que é
Este é um projeto Django que demonstra o envio de mensagens através do Django e o recebimento dessas mensagens pelo Flask usando o RabbitMQ como intermediário. O objetivo é mostrar como enviar mensagens assíncronas de uma aplicação para outra usando uma fila de mensagens.

### Como usar

Este projeto consiste em duas partes: uma aplicação Django que envia mensagens e uma aplicação Flask que recebe essas mensagens.  
![image](https://github.com/tiago3186/RabbitMQDemo/assets/132753395/84e6f163-ac40-480f-be0d-1a7553930260)

A aplicação Django possui uma rota que renderiza um formulário HTML onde você pode digitar uma mensagem. Quando você clica no botão "Enviar", a mensagem é enviada para o RabbitMQ usando a biblioteca pika. O RabbitMQ armazena a mensagem em uma fila chamada "messages".

A aplicação Flask possui um endpoint que está constantemente ouvindo a fila "messages" no RabbitMQ. Quando uma mensagem é recebida na fila, o Flask a imprime no terminal.  
![image](https://github.com/tiago3186/RabbitMQDemo/assets/132753395/55d81ad8-41fe-477c-bc47-7429b80e28ec)

Para que a comunicação entre as aplicações Django e Flask seja estabelecida, é necessário configurar corretamente as variáveis de ambiente no projeto Django. Essas variáveis especificam o host e a porta do RabbitMQ, bem como a URL do endpoint Flask. Mas no momento estão configuradas de um jeito bem básico e que funciona de forma geral.

Certifique-se de ter o RabbitMQ em execução localmente antes de executar.

Você pode acompanhar no seu localhost:15672 acessando pelo login e senha padrão guest / guest e ver o status dos envios das mensagens pelos canais padrão e os que você quiser configurar / adicionar:  
![image](https://github.com/tiago3186/RabbitMQDemo/assets/132753395/7f3b649d-ef8c-41ea-9e68-572d8953b22f)

