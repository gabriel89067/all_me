CC=g++
CFLAGS=-std=c++11 -Wall
TARGET=vpl_execution

BUILD_DIR    = ./build
SRC_DIR    = ./src
INCLUDE_DIR  = ./include

${TARGET}: ${BUILD_DIR}/Cilindro.o ${BUILD_DIR}/Circulo.o ${BUILD_DIR}/Ponto.o ${BUILD_DIR}/main.o
	${CC} ${CFLAGS} -o ${TARGET} ${BUILD_DIR}/*.o

${BUILD_DIR}/Cilindro.o: ${INCLUDE_DIR}/Cilindro.hpp ${SRC_DIR}/entidades/Cilindro.cpp
	${CC} ${CFLAGS} -I ${INCLUDE_DIR}/ -c ${SRC_DIR}/entidades/Cilindro.cpp -o ${BUILD_DIR}/Ferrari.o

${BUILD_DIR}/Circulo.o: ${INCLUDE_DIR}/Circulo.hpp ${SRC_DIR}/entidades/Circulo.cpp
	${CC} ${CFLAGS} -I ${INCLUDE_DIR}/ -c ${SRC_DIR}/entidades/Circulo.cpp -o ${BUILD_DIR}/Cilindro.o

${BUILD_DIR}/Ponto.o: ${INCLUDE_DIR}/Ponto.hpp ${SRC_DIR}/entidades/Ponto.cpp
	${CC} ${CFLAGS} -I ${INCLUDE_DIR}/ -c ${SRC_DIR}/entidades/Ponto.cpp -o ${BUILD_DIR}/Ponto.o

${BUILD_DIR}/main.o: ${INCLUDE_DIR}/Ponto.hpp ${INCLUDE_DIR}/Circulo.hpp ${INCLUDE_DIR}/Cilindro.hpp ${SRC_DIR}/main.cpp
	${CC} ${CFLAGS} -I ${INCLUDE_DIR}/ -c ${SRC_DIR}/main.cpp -o ${BUILD_DIR}/main.o

# Rule for cleaning files generated during compilation. 
# Call 'make clean' to use it
clean:
	rm -f ${BUILD_DIR}/* 
