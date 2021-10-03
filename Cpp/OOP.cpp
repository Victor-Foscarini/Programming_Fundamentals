#Victor-Foscarini

//Oriented Object for documentation

------------------------------------------------------------------------------------------------------------------------------------------
//sequência de collatz

#include <iostream>
using namespace std;

int main() {
    
    int ni,nf,ne,niarmazenado;
    int nim,nem;
        
    nim = 0;
    nem = 0;

// ni se refere ao numero inicial, nf ao numero final e ne ao numero de elementos relativo a esse numero inicial
//nim e nem sao os valores do ni de maior elemento e o numero de lementos deste
    
    for(ni=1;ni<=100000;ni++){
    
        ne = 1;
        
        niarmazenado = ni;
    
        while (ni !=1) {
    
            if (ni%2 == 0){
                nf = ni/2;
            }
            else{
                nf = 3*ni + 1;
            }
        
            ne += 1;
            ni=nf;
    
        };
        
        ni = niarmazenado;
        

        if (ne > nem){
            nem = ne;
            nim = ni;
        }
        
    }
    
    std::cout << "O numero de elementos de " << nim << " é " << nem << ".\n";

        
    return 0;

}

------------------------------------------------------------------------------------------------------------------------------------------
//intersecção de quadrado

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int main(){
    
    ifstream File("squares.dat");
    
    struct squares{
        string nome;
        float x,y,l;
    };
    
    vector <squares> results;
    
    //sabendo que o arquivo contem linhas com as informacoes acerca dos quadrados, elas serao lidas e salvas em uma struct
    //a struct eh salva em um vetor e o processo continua ate que nao tenha mais o que ser lido no arquivo
    
    while(!File.eof()){
        squares teste;
        File >> teste.nome >> teste.x >> teste.y >> teste.l;
        
        results.push_back(teste);
    }

    //entao serao comparados todos os quadrados salvos  e, no caso de interseccao, sera impirmida na tela os quadrados que intersectam e a area da interseccao
    //primeiro, sao salvos os menores e maiores valores de X e Y, e os lados l referente ao menor e L referente ao maior
    //entao eh realizada a comparacao, onde checa-se se os valores de menorX/Y e maiorX/Y sao diferentes e se ha intersecçao, ou seja, em ambos os eixos X e Y, a soma do menorX/Y com o lado l eh maior do que o maiorX/Y
    //por fim, para o calculo da area, compara-se a ponta direita dos quadrados (somando-se o valor da ponta esquerda, o menorX/Y com o valor do lado do quadrado), para X e Y 
    //a ponta da interseccao eh salva entao na variavel Grande e a area eh calculada
    
    
    float maiorX,menorX;
    float maiorY,menorY;
    float lX,lY;
    float LX,LY;
    float GrandeX,GrandeY;
    float Area;
    int max1 = results.size()-2;
    int max2 = max1+1;
    
    for (int i=0; i <= max1;i++){
        for(int j=i+1; j <= max2;j++){
            if (results[i].x > results[j].x){
                maiorX = results[i].x;
                menorX = results[j].x;
                lX = results[j].l;
                LX = results[i].l;
            }
            else{
                maiorX = results[j].x;
                menorX = results[i].x;
                lX = results[i].l;
                LX = results[j].l;
            }
            if (results[i].y > results[j].y){
                maiorY = results[i].y;
                menorY = results[j].y;
                lY = results[j].l;
                LY  = results[i].l;
            }
            else{
                maiorY = results[j].y;
                menorY = results[i].y;
                lY = results[i].l;
                LY = results[j].l;
            }
            
            if (menorX + lX > maiorX && menorY +lY > maiorY && menorX!=maiorX && menorY!=maiorY){
                if (menorX + lX > maiorX + LX){
                    GrandeX = maiorX + LX;
                }
                else{
                    GrandeX = menorX + lX;
                }
                if (menorY + lY > maiorY + LY){
                    GrandeY = maiorY + LY;
                }
                else{
                    GrandeY = menorY + lY;
                }
                Area = ( GrandeX - maiorX ) * ( GrandeY - maiorY );
                std :: cout << results[i].nome << " intercepts " << results[j].nome << " with area " << Area << endl;
            }
            
        }
    }
}

------------------------------------------------------------------------------------------------------------------------------------------
//contador limitado

#include <iostream>
#include "limited_counter.hpp"


void test_value(std::string test, int got, int expected) {
  if (got == expected) {
    std::cout << "OK " << test << std::endl;
  }
  else {
    std::cerr << "ERROR " << test
              << ": Got " << got << " but expected " << expected << std::endl;
  }
}

int main(int, char const *[]) {
  Limited_Counter c1(1, 10);
  test_value("initial value", c1.value(), 1);
  c1.up();
  test_value("up by one", c1.value(), 2);
  c1.down();
  test_value("down by one", c1.value(), 1);
  c1.up_by(5);
  test_value("up by value in limit", c1.value(), 6);
  c1.down_by(3);
  test_value("down by value in limit", c1.value(), 3);
  c1.up_by(-2);
  test_value("up by negative value in limit", c1.value(), 1);
  c1.down_by(-7);
  test_value("dowm by negative value in limit", c1.value(), 8);
  for (int i = 0; i < 100; ++i) {
    c1.up();
  }
  test_value("up out of limit", c1.value(), 10);
  for (int i = 0; i < 100; ++i) {
    c1.down();
  }
  test_value("down out of limit", c1.value(), 1);
  c1.up_by(37);
  test_value("up by out of limit", c1.value(), 10);
  c1.down_by(130);
  test_value("down by out of limit", c1.value(), 1);
  c1.up_by(-100);
  test_value("up by negative out of limit", c1.value(), 1);
  c1.down_by(-300);
  test_value("down by negative out of limit", c1.value(), 10);

  Limited_Counter c2(15);
  test_value("default initial value", c2.value(), 0);
  c2.down();
  test_value("default minimum value", c2.value(), 0);
}

------------------------------------------------------------------------------------------------------------------------------------------
//contador limitado

#include <iostream>

using namespace std;

class Limited_Counter{//declara-se uma classe contendo um valor n, os limites a inferior e b superior
    int n;            
    int a;
    int b;
    void normalize(){ //função normalizadora para garantir que n esteja dentro do limites 
        if (n>b){
            n = b;
        }
        else if (n<a){
            n = a;
        }
    }
    public:
        int value(){ //função que retorna o valor de n
            return n;
        }
        
        Limited_Counter(int a=0,int b=0){ //declaração do objeto e garantia de que a e b sejam,respectivamente, inferior e superior
            if (b>a){
                this->a = a;
                this->b = b;
                n = a;
            }
            else{
                this->a = b;
                this->b = a;
                n = b;
            }
        };
        //abaixo é feita a sobrecarga de operadores,sendo declarado um significado de algumas operações com classes
        Limited_Counter& operator+=(int num){ //operador +=
            this->n +=  num;
            normalize();
            return *this;
        }
        Limited_Counter& operator-=(int num){ //operador -=
            this->n -= num;
            normalize();
            return *this;
        }
        Limited_Counter operator++(){ //pré-incremento
            this->n ++;
            normalize();
            return *this;
        }
        Limited_Counter operator--(){ //pré-decremento
            this->n --;
            normalize();
            return *this;
        }
        Limited_Counter operator++(int){ //pós-incremento
            Limited_Counter anterior{*this};
            this->n ++;
            normalize();
            return anterior;
        }
        Limited_Counter operator--(int){//pós-decremento
            Limited_Counter anterior{*this};
            this->n --;
            normalize();
            return anterior;
        }
};

------------------------------------------------------------------------------------------------------------------------------------------
//template queue

#include <iostream>
#include <memory>
#include <vector>



template<class Type> 

//utiliza-se um template para que a classe Queue seja capaz de lidar com vários tipos de variáveis e não só inteiros
//para tal, é necessário atualizar as variáveis int dentro da classe para "Type", que foi definida no template

//na questão das exceções, utiliza-se um "try" nas funções pop() e front() para checar se o vetor não está vazio antes de proceder com as respectivas funções
//no caso de que o vetor esteja vazio, utiliza-se o "throw" com um número dado para o erro

class Queue {
  struct Node {
    Type value;
    std::unique_ptr<Node> next;
  };

  std::unique_ptr<Node> _front;
  Node *_back{nullptr};

public:

  void push(Type v);

  void pop();

  Type front() const;

  bool is_empty() const;
};


//aqui, ao se especificar o que fazem as funções definidas na classe, note que é necessário definir o template novamente

template<class Type>
void Queue<Type>::push(Type v) {
  Node *new_node = new Node{v, nullptr};
  if (_back) {

    _back->next.reset(new_node);
  } else {

    _front.reset(new_node);
  }

  _back = new_node;
}


template<class Type>
void Queue<Type>::pop() {
    try{
        if (is_empty()){ 
            throw 10; 
        }
        else{
            _front = std::move(_front->next);
             if (_front.get() == nullptr) {
            _back = nullptr;
        
            }
        }
    }catch(int y){ 
        std::cout<<"Tentando fazer pop em uma fila vazia: ERRO "<<y<<"\n"; 
        
    }
}

template<class Type>
Type Queue<Type>::front() const { 

    try{
        if (is_empty()){ 
            throw 20; 
        }
        else{
            return _front->value; 
        }
    }catch(int x){ 
        std::cout<<"Tentando fazer um front em uma fila vazia: ERRO "<<x<<"\n"; 
        
    }
}


template<class Type>
bool Queue<Type>::is_empty() const { return _front.get() == nullptr; }

// Alguns testes simples.
//Note que, como foi utilizado template, é necessário especificar o tipo de variável utilizada ao se definir uma classe
//No caso da classe "my_queue, foi utilizado int"

int main(int, char const *[]) {

      Queue<int> my_queue;
      for (int i = 0; i < 4; ++i) {
        my_queue.push(i);
      }
      std::cout << "Primeiro na fila: " << my_queue.front() << std::endl;
      my_queue.pop();
      for (int i = 0; i < 3; ++i) {
        my_queue.push(3 * i);
      }
    
      std::cout << "Fila atual: ";
      while (!my_queue.is_empty()) {
        auto x = my_queue.front();
        my_queue.pop();
        std::cout << x << " ";
      }
      std::cout << std::endl;
      
}

------------------------------------------------------------------------------------------------------------------------------------------

