#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char element;

typedef struct node {
    element data;
    struct node * left;
    struct node * right;
} node;

node* makeRoot(element data, node* left, node* right) {
    node* root = (node*)malloc(sizeof(node));
    root->data = data;
    root->left = left;
    root->right = right;
    return root;
}

void preorder(node *root) {
    if (root) {
        printf("%c", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void inorder(node *root) {
    if (root) {
        inorder(root->left);
        printf("%c", root->data);
        inorder(root->right);
    }
}

void posorder(node *root) {
    if (root) {
        posorder(root->left);
        posorder(root->right);
        printf("%c", root->data);
    }
}

int main() {
    node* n7 = makeRoot('7', NULL, NULL);
    node* n6 = makeRoot('6', NULL, NULL);
    node* n5 = makeRoot('5', NULL, NULL);
    node* n4 = makeRoot('4', NULL, NULL);
    node* n3 = makeRoot('3', n6, n7);
    node* n2 = makeRoot('2', n4, n5);
    node* n1 = makeRoot('1', n2, n3);

    preorder(n1);
    printf("\n");
    inorder(n1);
    printf("\n");
    posorder(n1);
    return 0;
}