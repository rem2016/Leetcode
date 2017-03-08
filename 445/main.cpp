#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<algorithm>
#include<vector>
#include<list>
#define null NULL

using namespace std;
struct ListNode{
	int val;
	ListNode *next;
};


class Solution {
public:
	int countLength(ListNode* l){
		int  i;
		for (i = 1; l->next != null; i++, l=l->next);
		return i;
	}
	ListNode* update(ListNode* next, ListNode* pre ){
		if (next == null) return null;
		update(next->next, next);
		if (next -> val > 9){
			int c = next->val / 10;
			if (pre == null){
				next->val = next->val % 10;
				pre = (ListNode*)malloc(sizeof(ListNode));
				pre->next = next;
				pre->val = c;
			}else{
				pre->val += c;
				next->val = next->val % 10;
			}
		}
		if(pre == null){
		    return next;
		}
		return pre;
	}
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		int length1 = countLength(l1);
		int length2 = countLength(l2);
		if (length1 < length2){
			swap(l1, l2);swap(length1, length2);
		}
		printf("%d  %d\n", length1, length2);
		ListNode* ll2 = l2;
		ListNode* ll1 = l1;
		ListNode* newl = (ListNode*) malloc(sizeof(ListNode));
		ListNode* iter_new = newl, *pre=null;
		newl -> next = null;
		for ( int i = length1 - length2; i > 0; i--, ll1 = ll1->next){
			iter_new -> val = ll1->val;
			printf("%d\n", iter_new->val);
			iter_new -> next = (ListNode*) malloc(sizeof(ListNode));
			pre = iter_new;
			iter_new = iter_new->next;
			iter_new -> next = null;
			iter_new -> val = 0;
		}
		for( int i = length2; i > 0; i--, ll2 = ll2->next, ll1=ll1->next){
			iter_new -> val = ll1->val + ll2->val;
			printf("%d\n", iter_new->val);
			iter_new -> next = (ListNode*) malloc(sizeof(ListNode));
			pre = iter_new;
			iter_new = iter_new->next;
			iter_new -> next = null;
			iter_new -> val = 0;
		}
		pre -> next = null;
		return update(newl, null);
    }
};
int main(){
	
	
}
