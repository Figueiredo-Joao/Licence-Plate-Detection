

# Projeto de Estágio


## Descrição:

Criar um sistema que através do livefeed de uma webcam juntamente com uma rede neural, identifique se o feed contém uma matricula e enviar via web para a api criada pela Makewise retorne os dados contidos na matricula.


### Software:
 - Visual Studio Code;

### Tecnologias:
- Python;
- TensorFlow Lite (tflite);
- Keras;
- Git;
	
## Passos:
 1. Criar uma rede neural utilizando o Keras que identifique existência matriculas;
 2. Converter a rede neural num modelo TensorFlowlite;
 3. Criar um programa utilizando o IDE Visual Studio Code com a liguagem de programação Python que capture o feed da webcam do computador e processe com o modelo da rede;
 4. Caso o modelo identifique a existência de matricula no feed de video enviar imagem via web para a api da Makewise para esta retorne os dados contidos na matricula.
