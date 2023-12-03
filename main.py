import networkx as nx
import matplotlib.pyplot as plt
#Diego Menegaz 12/2/2023 11:19PM
#There was no available file submission section + I don't know your github matches the screenshot so should excuse the public github repo.
class Person:
    def __init__(self, name, c1,c2,c3,c4,c5,c6):
        self.name = name
        self.choices = [c1,c2,c3,c4,c5,c6]
def main():
    Votes = [[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]
    par1 = Person('Kaylee',2,1,5,4,3,6)
    par2 = Person('Leif', 1, 2, 5, 4, 3, 6)
    par3 = Person('Olivia', 1, 2, 5, 4, 6, 3)
    par4 = Person('Josh', 1, 2, 5, 4, 6, 3)
    par5 = Person('Anthony', 1, 2, 5, 4, 6, 3)
    Boxes = ['Background_Video','Calendar','Appt_Add','G_Maps','Search','Reminders']
    T = nx.DiGraph()
    for i in range(1,6):
        T.add_node(i)
    T.add_edge(1,2,weight=1)
    T.add_edge(2, 5, weight=2)
    T.add_edge(5, 4, weight=3)
    T.add_edge(4,6,weight=4)
    T.add_edge(6, 3, weight=5)
    options = {
        'node_color': 'blue',
        'node_size': 300,
        'width': 3,
        'arrowstyle': '-|>',
        'arrowsize': 12,
    }
    node_labels = {1: Boxes[0], 2: Boxes[1], 3: Boxes[2], 4: Boxes[3],5:Boxes[4],6:Boxes[5]}
    pos = nx.spring_layout(T)
    nx.draw_networkx(T,pos,  arrows=True, with_labels=True, labels=node_labels, **options)
    plt.show()
if __name__ == "__main__":
    main()