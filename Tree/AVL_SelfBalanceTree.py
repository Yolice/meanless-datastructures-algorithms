class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.bf=None
        self.height=None
        self.parent=None


class Self_Balance_BST:
    def __init__(self):
        self.root=None
        self.balance_fator=[1,0,-1]
        self.count=1
        self.height=0
        self.critial_node=[]


    def Get_root(self):
        return self.root


    def Create_SelfBalanceTree(self,data):
        if self.root is None:
            self.root=TreeNode(data)
        else:
            self.add_node(self.root,data)


    def add_node(self,root,data):
        if data < root.data :
            if root.left:
                self.add_node(root.left,data)
            else:
                children=TreeNode(data)
                children.parent=root
                root.left=children
                self.Rotation()
        elif data > root.data:
            if root.right:
                self.add_node(root.right,data)
            else:
                children=TreeNode(data)
                children.parent=root
                root.right=children
                self.Rotation()
        else:
            return False




    def Rotation(self):
        #print("-----开始")
        #self.PreTraversal(self.root)
        self.CheckBF(self.root)
        #print("此时根为"+str(self.root.data))
        #for i in self.critial_node:
            #print(str(i.data)+"为当前不平衡因子")
        if self.critial_node:
            #print("开始执行旋转")
            inbalance_node = self.critial_node.pop()
            self.critial_node = []
            #print("取出的不平衡因子值为"+str(inbalance_node.data))
            if inbalance_node.bf == 2 and inbalance_node.left.bf == 1:
                self.LL_Rotation(inbalance_node)
                #print("a")
            elif inbalance_node.bf == 2 and inbalance_node.left.bf == -1:
                self.LR_Rotation(inbalance_node)
                #print("b")
            elif inbalance_node.bf == -2 and inbalance_node.right.bf == 1:
                self.RL_Rotation(inbalance_node)
                #print("c")
            elif inbalance_node.bf == -2 and inbalance_node.right.bf == -1:
                self.RR_Rotation(inbalance_node)
                #print("d")
            self.reset_root(inbalance_node)
            #self.CheckBF(self.root)
            #print("旋转后根为"+str(self.root.data))
            #print("前序遍历为")
            #self.PreTraversal(self.root)
            #print("-----结束")


    def PreTraversal(self,root):
        if root:
            print(root.data)
            self.PreTraversal(root.left)
            self.PreTraversal(root.right)



    def RearTraversal(self,root):
        if root:
            self.RearTraversal(root.left)
            self.RearTraversal(root.right)
            print(root.data)



    def MidTraversal(self,root):
        if root:
            self.MidTraversal(root.left)
            print(root.data)
            self.MidTraversal(root.right)


    def LL_Rotation(self,node):    ##当失衡节点bf为2且其左子树bf为1时用LL旋转
        inbalance_left_node=node.left
        temple_node=inbalance_left_node.right      ##暂时存放要交换的节点
        if node == self.root:
            node.parent=inbalance_left_node
            self.root=inbalance_left_node
            inbalance_left_node.parent=None
        else:
            if node.parent.data>node.data:     ##一定要判断是父节点的左或者右儿子
                node.parent.left=inbalance_left_node
            else:
                node.parent.right=inbalance_left_node
            inbalance_left_node.parent=node.parent
            node.parent = inbalance_left_node
        inbalance_left_node.right=node
        node.left = temple_node
        if temple_node:
            temple_node.parent=node



    def RR_Rotation(self,node):  ##当失衡节点bf为-2且其右子树bf为-1时候RR旋转
        inbalance_right_node=node.right
        temple_node=inbalance_right_node.left
        if node == self.root:
            node.parent=inbalance_right_node
            self.root=inbalance_right_node
            inbalance_right_node.parent=None
        else:
            if node.parent.data>node.data:
                node.parent.left=inbalance_right_node
            else:
                node.parent.right=inbalance_right_node
            inbalance_right_node.parent = node.parent
            node.parent = inbalance_right_node
        inbalance_right_node.left=node
        node.right = temple_node
        if temple_node:
            temple_node.parent=node


    def RL_Rotation(self,node): ##当失衡节点bf为-2且其右子树bf为1时候RL旋转
        inbalance_right_node=node.right
        inbalance_right_node_left_child=inbalance_right_node.left
        temple_node=inbalance_right_node_left_child.right
        inbalance_right_node.parent.right=inbalance_right_node_left_child
        inbalance_right_node_left_child.parent=node
        inbalance_right_node_left_child.right=inbalance_right_node
        inbalance_right_node.parent=inbalance_right_node_left_child
        inbalance_right_node.left=temple_node
        if temple_node:
            temple_node.parent=inbalance_right_node
        self.RR_Rotation(node)

    def LR_Rotation(self,node): ##当失衡节点为2且左子树bf为-1时候LR旋转
        inbalance_left_node=node.left
        inbalance_left_node_right_child=inbalance_left_node.right
        temple_node=inbalance_left_node_right_child.left
        inbalance_left_node.parent.left=inbalance_left_node_right_child
        inbalance_left_node_right_child.parent=inbalance_left_node.parent
        inbalance_left_node_right_child.left=inbalance_left_node
        inbalance_left_node.parent=inbalance_left_node_right_child
        inbalance_left_node.right=temple_node
        if temple_node:
            temple_node.parent=inbalance_left_node
        self.LL_Rotation(node)




    def CheckBF(self,root):
        if root:
            bf=self.Get_node_balancefator(root,self.count)
            root.bf=bf
            #print(str(root.data)+" bf is "+str(bf))
            if bf not in self.balance_fator:
                #print("当前我得到了不平衡因子值为" + str(root.data))
                self.critial_node.append(root)
            self.CheckBF(root.left)
            self.CheckBF(root.right)




    def Get_node_balancefator(self,root,count):
        if root:     ##一切建立在这个节点是存在的情况下
            leftheight=self.PrintHeight(root.left,count)
            self.height=0
            rightheight=self.PrintHeight(root.right,count)
            self.height=0
            if leftheight is None and rightheight is None:
                return 0
            if leftheight is None and rightheight:
                leftheight=0
            if rightheight is None and leftheight:
                rightheight=0
            return leftheight-rightheight


    def PrintHeight(self,root,count):   ##函数在递归回归到前一个函数的的时候，当前保存的count值正好对应当前高度值。
        if root:
            if count > self.height:
                self.height=count
            self.PrintHeight(root.left,count+1)
            self.PrintHeight(root.right,count+1)
            return self.height        ##这里没有在递归函数上写return是因为不用接力回归的值，此时函数执行到最后必有一个return不像之前查值时候用if分割了3总情况


    def SearchNode(self,data):
        if self.root is None:
            return False
        else:
            return self.SearchStep(self.root,data)      ##从这行开始，到下面searchstep函数都需要return接力返回结果，递归后的函数如果没有return默认返回None




    def SearchStep(self,root,data):
        if root.data == data:
            return root
        elif data < root.data and root.left is not None:
            return self.SearchStep(root.left,data)         ##必须要return
        elif data > root.data and root.right is not None:
            return self.SearchStep(root.right,data)    ##必须要return


    def FreeNode(self,node):
        node.left=None
        node.right=None
        node.parent=None



    def FindMinNode(self,root):
        if root.left:
            return self.FindMinNode(root.left)
        elif root.left is None:
            return root



    def FindMaxNode(self,root):
        if root.right:
            return self.FindMaxNode(root.right)   ##树是一种递归性质的结构，所以在获取树中的一个节点时候要接力return的值
        elif root.right is None:
            return root




    def DeleteTreeNone(self,data):   ##作为一种简单的方法，可以交换被删除节点的值和代替节点的值，然后删除代替节点
        node=self.SearchNode(data)
        if node:
            if node.left and node.right:   ##假如要删除的节点左右子树都存在的情况
                replace_node=self.FindMinNode(node.right)
                replace_node.left=node.left
                replace_node.right=node.right
                if node.data == self.root.data:            ##要删除的是根节点的情况
                    replace_node.parent.left=None          ##如果写replace_node.parent=None,那么parent的left依旧链接replacenode，所以要写出parent.left链向目标
                                                           ##因为二叉树的特性，replace节点一定是父节点的左子树，所以replacenode.parent.left=None即可以切断链接，最后节点由python回收机制回收
                    self.FreeNode(node)
                    self.root=replace_node                 ##如果删除是根节点，那么代替节点就是新的根节点00

                else:                                      ##在删除之前要找到被删除点是左子树或者是右子树
                    if node.parent.left and node.parent.left.data == node.data:
                        replace_node.parent.left=None
                        node.parent.left=replace_node
                        self.FreeNode(node)
                    elif node.parent.right and node.parent.right.data == node.data:
                        replace_node.parent.left=None
                        node.parent.right=replace_node
                        self.FreeNode(node)
            elif node.left and node.right is None:   ##只有单一左子树存在时候
                if node.parent.left and node.parent.left.data == node.data:   ##判断左子树或者右紫薯
                    node.parent.left=node.left
                    self.FreeNode(node)
                elif node.parent.right and node.parent.right.data == node.data:
                    node.parent.right=node.left
                    self.FreeNode(node)
            elif node.right and node.left is None:
                if node.parent.left and node.parent.left.data == node.data:
                    node.parent.left=node.right
                    self.FreeNode(node)
                elif node.parent.right and node.parent.right.data == node.data:
                    node.parent.right=node.right
                    self.FreeNode(node)
            elif node.left is None and node.right is None:  ##如果没有左右子树
                if node.parent.left and node.parent.left.data == node.data:
                    node.parent.left=None
                    self.FreeNode(node)
                elif node.parent.right and node.parent.right.data == node.data:
                    node.parent.right=None
                    self.FreeNode(node)
            self.Rotation()

        else:
            return False  ##没有找到节点删除失败





    def reset_root(self,node):
        if node.parent:
            self.reset_root(node.parent)
        else:
            self.root=node


'''
a=Self_Balance_BST()


a.Create_SelfBalanceTree(3)
a.Create_SelfBalanceTree(2)
a.Create_SelfBalanceTree(1)
a.Create_SelfBalanceTree(4)
a.Create_SelfBalanceTree(5)
a.Create_SelfBalanceTree(6)
a.Create_SelfBalanceTree(7)
a.Create_SelfBalanceTree(16)
a.Create_SelfBalanceTree(15)
a.Create_SelfBalanceTree(14)
a.Create_SelfBalanceTree(13)
a.Create_SelfBalanceTree(12)
a.Create_SelfBalanceTree(11)
a.Create_SelfBalanceTree(10)
a.Create_SelfBalanceTree(8)
a.Create_SelfBalanceTree(9)

测试全部通过！
'''
