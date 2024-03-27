#include<deque>
class MyStack {
 deque<int> q;
public:
    MyStack() {
    
    }
    
    void push(int x) {
    q.push_front(x);
    }
    
    int pop() {
       if(empty()){
       return -1;
       }
   int last=q.front();
       q.pop_front();
     return last;   
    }
    
    int top() {
    if(empty()){
        return -1;
    }
        else return q.front();
    }
    
    bool empty() {
     if(q.empty()){
        return 1;
        }
    else return 0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */