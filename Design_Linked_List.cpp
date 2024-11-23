struct Node {
 int data;
 Node * next;
};
class MyLinkedList {
public:
Node * head;
Node * tail;

    MyLinkedList() {
        head =NULL;
        tail = NULL;

        
    }
    
    int get(int index) {
        int i = 0;
        Node * temp = head;
        if(head == NULL){
            return -1;
        }
        while(temp != NULL){
            if(i == index){
                return  temp->data;
                
            }
            temp = temp->next;
            i++;
        }
        return -1;
        
    }
    
    void addAtHead(int val) {
        Node * temp = new Node();
        temp->data = val;
        temp->next = head;
        head = temp;
        if(tail == NULL){
            tail = temp;
        }
        
    }
    int getl(){
        int i = 0;
        Node *temp =head;
        while(temp != NULL){
            i++;
            temp = temp->next;
        }
        return i;
    }
    
    void addAtTail(int val) {
        Node * temp = new Node();
        temp->data = val;
        temp->next = NULL;
        if(head == NULL){
            head = temp;
            tail = temp;
        }
        else{
            tail->next = temp;
            tail = temp;
        }
        
    }
    
    void addAtIndex(int index, int val) {
        if(index == 0){
            addAtHead(val);
            return ;
        }
        if(index == getl()){
            addAtTail(val);
            return;
        }
        if(index >getl()){
            return ;
        }
        Node * temp = head;
        Node * prev = NULL;
        int i = 0;
        while(temp != NULL){
            if(i == index){
                Node * new_node = new Node();
                new_node->data = val;
                new_node->next = temp;
                prev->next = new_node;
                return ;
            }
            i++;
            prev = temp;
            temp = temp->next;



        }

        
    }
    
    void deleteAtIndex(int index) {
    if (index < 0 || head == nullptr) { // Invalid index or empty list
        return;
    }

    if (index == 0) { 
        Node* temp = head;
        head = head->next;
        if(head == NULL){
            tail = NULL;
        }
        delete temp;
        return;
    }

    Node* current = head;
    for (int i = 0; i < index - 1 && current->next != nullptr; ++i) {
        current = current->next;
    }

    if (current->next == nullptr) { 
        return;
    }

    Node* temp = current->next;
    current->next = temp->next;
    if (temp == tail) { // If the last node is being deleted
        tail = current;
    }

    delete temp;
}

};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
