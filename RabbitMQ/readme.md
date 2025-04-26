# RabbitMQ on MacBook

##  What is RabbitMQ?
RabbitMQ is an open-source **message broker** that enables applications to communicate asynchronously using message queues. It decouples services, handles traffic spikes, and ensures reliable message delivery.

### Key Concepts:
- **Producer**: Application that sends messages
- **Consumer**: Application that receives messages  
- **Queue**: Temporary storage for messages
- **Exchange**: Routes messages to queues (Types: Direct, Fanout, Topic, Headers)

## 🛠 Installation (Mac)
```bash
# Using Homebrew
# RabbitMQ on MacBook

Guide to install, manage, and troubleshoot RabbitMQ on macOS.

## 🛠 Installation

# Install RabbitMQ
brew update
brew install rabbitmq

# Add RabbitMQ to PATH
echo 'export PATH="/usr/local/sbin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Start RabbitMQ
brew services start rabbitmq

# Enable Management Plugin (Web UI)
rabbitmq-plugins enable rabbitmq_management

Access Web UI at: http://localhost:15672
Default credentials: guest/guest

Action	Command
Start	            brew services start rabbitmq
Stop	            brew services stop rabbitmq
Restart	            brew services restart rabbitmq
Check Status	    `brew services list	grep rabbitmq`
Force               Stop	kill -9 $(pgrep -f rabbitmq)	(NEWLY ADDED)
List                Queues	rabbitmqctl list_queues

rabbitmqctl change_password username newpassword