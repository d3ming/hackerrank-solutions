/*https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/copy-from/17942742*/

/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;
*/

node * lca(node * root, int v1, int v2)
{   
    if(root == NULL)
    {
        return NULL;
    }
    
    int smallV = min(v1, v2);
    int largeV = max(v1, v2);
    int rootV = root->data;
    
    if(rootV >= smallV && rootV <= largeV)
    {
        return root;
    }
    else if(rootV > largeV)
    {
        if(root->left == NULL){
            return root;
        }
        return lca(root->left, smallV, largeV);
    }else
    {
        if(root->right == NULL)
        {
            return root;
        }
        return lca(root->right, smallV, largeV);
    }
}
