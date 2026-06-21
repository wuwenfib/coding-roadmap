/*
    203. 移除链表元素
    简单
    相关标签
    premium lock icon
    相关企业
    给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
    

    示例 1：


    输入：head = [1,2,6,3,4,5,6], val = 6
    输出：[1,2,3,4,5]
    示例 2：

    输入：head = [], val = 1
    输出：[]
    示例 3：

    输入：head = [7,7,7,7], val = 7
    输出：[]
    

    提示：

    列表中的节点数目在范围 [0, 104] 内
    1 <= Node.val <= 50
    0 <= val <= 50
*/

#include <iostream>


using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* removeElements(ListNode* head, int val) {
    ListNode * node = new ListNode(0);
    node->next = head;
    ListNode * h = node;
    while(node->next){
        if(node->next->val == val){
            node->next = node->next->next;
            continue;
        }
        node=node->next;
    }       
    return h->next; 
}

int main(){
    ListNode * node = new ListNode(1);
    node->next = new ListNode(2);
    node->next->next = new ListNode(6);
    node->next->next->next = new ListNode(3);
    node->next->next->next->next = new ListNode(3);
    node->next->next->next->next->next = new ListNode(3);
    node->next->next->next->next->next->next = new ListNode(3);
    removeElements(node,6);
    return 0;
}