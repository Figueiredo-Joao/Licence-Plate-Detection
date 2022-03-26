

# Projeto de Estágio


## Descrição:

Criar um sistema que através do livefeed de uma webcam juntamente com um modelo de uma rede neural, identifique se o feed contém uma matricula e enviar via web para a api criada pela Makewise para que esta retorne os dados contidos nas matriculas identificadas.


### Software:
 - Visual Studio Code;
 - Google Colab.

### Tecnologias:
- Python;
- TensorFlow Lite (tflite);
- Keras;
- Git.
	
## Passos:
 1. Criar um programa utilizando a linguagem de programação Python que utilize um conjunto de várias imagens de veículos com matricula e sem matricula e, que o mesmo faça um crop na zona onde está situada a matricula e outro numa zona aleatória na imagem com o propósito de criar um dataset para treino.
 1. Com o dataset criado e utilizando a plataforma Google Colab em conjunto com o Tensorflow Keras criar um modelo de rede neural que identifique existência matriculas em imagens.
 1. Treinar o modelo de rede neural com diversos tipos de camadas de augmentation para melhorar a precisão do modelo de rede.
 1. Converter o modelo de rede neural num modelo TensorFlowlite para diminuir o seu tamanho.
 1. Criar um programa utilizando em Python que capture o feed da webcam do computador e em conjunto com o modelo de rede indentifique se a imagem que está a ser capturada contém matricula ou não.
 1. Utilizar a api da Makewise para esta retorne os dados contidos nas matriculas identificadas pelo sistema.
