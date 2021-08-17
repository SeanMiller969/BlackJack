FROM python:3.9
RUN pip install numpy
RUN mkdir project
RUN cd project
RUN git clone https://github.com/SeanMiller969/BlackJack
EXPOSE 5000
