#include <iostream>
using namespace std;

//Binary Search Tree Node Structure

struct Node{
    int value;
    
    Node *right;
    Node *left;
    
    Node(int value){
        this->value = value;
        this->right = NULL;
        this->left = NULL;
    }
};

//Binary Search Tree class

class BST{
    
    private:
    
    Node *root; //root Node
    void insert(Node *root, int value); //insert private operation
    bool remove(Node *parent, Node *current, int value); //remove private operation
    Node* nextLarger(Node *node); //find next larger node for deletion
    Node* findNodeWithValue(int value); //find node with given value
    void print(Node *node); //printing
    
    public:
    
    void insert(int value);
    bool remove(int value);
    Node *findMin(); //find node with minimum value
    Node *findMax(); //find node with maximum value
    Node *getRoot(); //return root Node
    void printTree();

};

Node* BST::findNodeWithValue(int value){
    Node *current = root; //save the current node, starting with root
    while(current){ //loop for left/right node while current node is not NULL
        if(current->value = value){
            break;
        }else if (value > current->value){
            current = current->right;
        }else {
            current = current->left;
        }
    }
    return current;
}

Node* BST::nextLarger(Node *node){
    Node *nextLarger = node->right; //start with the right node
    while (nextLarger->left){ // get left node while it's not null
        nextLarger = nextLarger->left;
    }
    return nextLarger;
}

void BST::insert(Node *root, int value){
    if (value > root->value){ //higher than root
        if(!root->right){ //if root->right is NULL
            root->right = new Node(value); //insert value on the right of the root
        }else{ 
            insert(root->right,value); //go deeper
        }
    }else{ //lower than root
        if(!root->left){ //if root->left is NULL
            root->left = new Node(value); //insert value on the left of the root
        }else{ 
            insert(root->left,value); //go deeper
        }
    }
}

bool BST::remove(Node *parent, Node *current, int value){ //give parent and current is suppose to be the child to be removed
    if (!current){
        return false; //did not find any node with given value
    }
    if (current->value == value){ //Right node to remove
        if (!current->left && !current->right){ //node is leaf -> remove and return
            if (parent->right == current){
                parent->right = NULL;
            }else{
                parent->left = NULL;
            }
            delete current;
            current = NULL;
            return true;
        }
        else if(!current->left || !current->right){ //check if node has only one child
            Node *child = current->left; //get the only child
            if (!child){
                child = current->right;
            }
            if (!parent){ //if deleting root node, child becomes root
                this->root = child;
            }else{ //parent now points to current's child
                if (child->value > parent->value){
                    parent->right = child;
                }
                else{
                    parent->left = child;
                }
            delete current;
            current = NULL;
            }
        }else{ //current has two children
            Node *nextLargerNode = nextLarger(current); //get next larger node from current
            current->value = nextLargerNode->value; //set nextLargerNode into current node
            delete nextLargerNode; //MISTAKE HERE -> next larger node is not always a leave
            nextLargerNode = NULL;
        }
        return true;
    }
    
    if(value > current->value){ //not right node to remove
        return remove(current,current->right,value);
    }else{
        return remove(current,current->left,value);
    }    
}

void BST::print(Node *root){
    if (!root){
        return;
    }
    print(root->left);
    std::cout<< root->value << " ";
    print(root->right);
}

void BST::insert(int value){
    if(!root){
        root = new Node(value);
    }else{
        this->insert(root,value);
    }
}

void BST::printTree(){
    if (!root){
        return;
    }
    print(root);
    std::cout << endl;
}


Node* BST::findMax(){
    Node *max = root;
    while(max->right){
        max = max->right;
    }
    return max;
}

Node* BST::findMin(){
    Node *min = root;
    while(min->left){
        min = min->left;
    }
    return min;
}

bool BST::remove(int value){
    return remove(NULL,root,value);
}

int main() {
    BST *bst = new BST();
    
    for (int i=0;i<=100;i++){ //generate tree
        bst->insert(rand()%100);
    }
    
     // Add nodes
    bst->insert(10);
    bst->insert(20);
    bst->insert(25);
    bst->insert(8);
    bst->insert(9);
    bst->insert(2);
    bst->insert(4);
    bst->insert(1);
    bst->insert(3);
    
    bst->printTree(); //print sorted tree
    std::cout << std::endl;
    
    Node *max = bst->findMax(); //find max
    cout << "Max node: " << max->value << endl;

    Node *min = bst->findMin(); //find min
    cout << "Min node: " << min->value << endl;

    cout << endl;


    cout << "Removing: 9" << endl; //remove leaf
    bst->remove(9);
    bst->printTree();

    cout << "Removing: 4" << endl; // remove node with 1 child
    bst->remove(4);
    bst->printTree();

    cout << "Removing: 8" << endl; // remove node with 2 children
    bst->remove(8);
    bst->printTree();
}
