from PyQt5.QtCore import QCoreApplication, Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel

class PyElementorApp(QObject):
    def __init__(self, title="PyElementor App", size=(800, 600)):
        """Inicializa o aplicativo"""
        super().__init__()  # Chama o construtor da classe QObject
        self.app = QApplication([])  # Inicializa a aplicação PyQt5
        self.window = QMainWindow()  # Cria a janela principal
        self.window.setWindowTitle(title)  # Define o título da janela
        self.window.resize(*size)  # Redimensiona a janela com o tamanho fornecido

        # Criando o layout central sem bordas extras
        central_widget = QWidget(self.window)
        central_layout = QVBoxLayout(central_widget)
        central_layout.setContentsMargins(0, 0, 0, 0)  # Remove as margens internas

        # Área para renderizar HTML
        self.view = QWebEngineView(self.window)  # Cria a visualização de HTML
        central_layout.addWidget(self.view)  # Adiciona o QWebEngineView ao layout
        self.window.setCentralWidget(central_widget)  # Define a área central da janela

        # Inicializa o canal de comunicação
        self.channel = QWebChannel()
        self.channel.registerObject("python", self)  # Registra o objeto Python (que agora é QObject)
        self.view.page().setWebChannel(self.channel)  # Conecta o canal à página web

        # Dicionário de eventos
        self.events = {}

    def load_html(self, html_content):
        """Carrega o conteúdo HTML na janela"""
        self.view.setHtml(html_content)

    def trigger_event(self, event_name):
        """Método Python chamado pelo JavaScript quando o evento é disparado"""
        if event_name in self.events:
            self.events[event_name]()  # Chama a função de callback registrada

    def on_event(self, event_name, callback):
        """Registra eventos personalizados"""
        self.events[event_name] = callback

    def send_notification(self, message, notification_type="info"):
        """
        Envia uma notificação para o frontend.
        :param message: Texto da notificação.
        :param notification_type: Tipo da notificação (success, error, info).
        """
        script = f"""
        showNotification("{message}", "{notification_type}");
        """
        self.view.page().runJavaScript(script)

    def run(self):
        """Executa o loop de eventos do PyQt5"""
        self.window.show()  # Exibe a janela
        self.app.exec_()  # Inicia o loop do aplicativo


# Função para criar e inicializar um aplicativo PyElementor
def create_app(title="PyElementor App", size=None):
    """Função para criar e inicializar um aplicativo"""
    if size is None:
        size = (800, 600)  # Tamanho padrão, caso o usuário não forneça
    return PyElementorApp(title, size)
