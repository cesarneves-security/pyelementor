from pyelementor import create_app

# Cria a aplicação
app = create_app()

# Conteúdo HTML com CSS moderno e funcionalidade de login
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tela de Login</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #4e54c8, #8f94fb);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
        }

        .login-container {
            background: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 10px;
            width: 350px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            text-align: center;
            animation: fadeIn 1s ease-in-out;
        }

        .login-container h1 {
            margin-bottom: 20px;
            font-size: 24px;
            font-weight: bold;
        }

        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }

        .login-container input[type="submit"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background: #4e54c8;
            font-size: 18px;
            font-weight: bold;
            color: #fff;
            cursor: pointer;
            transition: background 0.3s ease-in-out;
        }

        .login-container input[type="submit"]:hover {
            background: #8f94fb;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    <script type="text/javascript">
        var python;

        // Inicializa o canal de comunicação com Python
        function initializeChannel() {
            python = new QWebChannel(qt.webChannelTransport, function (channel) {
                window.python = channel.objects.python;
            });
        }

        // Carrega o canal QWebChannel
        function loadQWebChannel() {
            var script = document.createElement('script');
            script.src = 'qwebchannel.js'; 
            script.onload = initializeChannel; 
            document.head.appendChild(script);
        }

        window.onload = loadQWebChannel;

        // Função de login
        function onLogin() {
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;
            
            if (python) {
                python.trigger_event('login', username, password);
            } else {
                console.error("Canal Python não está inicializado.");
            }
        }
    </script>
</head>
<body>
    <div class="login-container">
        <h1>Bem-vindo</h1>
        <input type="text" id="username" placeholder="Usuário" />
        <input type="password" id="password" placeholder="Senha" />
        <input type="submit" value="Login" onclick="onLogin()" />
    </div>
</body>
</html>
"""

# Carrega o conteúdo HTML
app.load_html(html_content)

# Registra evento de login
def on_login(username, password):
    print(f"Tentativa de login: Usuário={username}, Senha={password}")

app.on_event("login", on_login)

# Executa a aplicação
app.run()
