#include <iostream>
#include <list>
#include <stack>
#include <vector>
using namespace std;
vector<int> vec2;
vector<int> vec;

int Partition(vector<int>& v, int start, int end) {

    int pivot = end;
    int j = start;
    for (int i = start;i < end;++i) {
        if (v[i] > v[pivot]) {
            swap(v[i], v[j]);
            ++j;
        }
    }
    swap(v[j], v[pivot]);
    return j;

}

void Quicksort(vector<int>& v, int start, int end) {

    if (start < end) {
        int p = Partition(v, start, end);
        Quicksort(v, start, p - 1);
        Quicksort(v, p + 1, end);
    }

}

void printVector(vector<int> vec) {
    for (size_t i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    cout << endl;
}

class Graph {
    int V;
    list<int>* adj;
    void fillOrder(int s, bool visitedV[], stack<int>& Stack);
    void DFS(int s, bool visitedV[]);

public:
    Graph(int V);
    void addEdge(int s, int d);
    void printSCC();
    Graph transpose();
};

Graph::Graph(int V) {
    this->V = V;
    adj = new list<int>[V];
}

// DFS
void Graph::DFS(int s, bool visitedV[]) {
    visitedV[s] = true;
    vec2.push_back(s);
    list<int>::iterator i;
    for (i = adj[s].begin(); i != adj[s].end(); ++i)
        if (!visitedV[*i])
            DFS(*i, visitedV);
}

// Transpose
Graph Graph::transpose() {
    Graph g(V);
    for (int s = 0; s < V; s++) {
        list<int>::iterator i;
        for (i = adj[s].begin(); i != adj[s].end(); ++i) {
            g.adj[*i].push_back(s);
        }
    }
    return g;
}

// Add edge into the graph
void Graph::addEdge(int s, int d) {
    adj[s].push_back(d);
}

void Graph::fillOrder(int s, bool visitedV[], stack<int>& Stack) {
    visitedV[s] = true;

    list<int>::iterator i;
    for (i = adj[s].begin(); i != adj[s].end(); ++i)
        if (!visitedV[*i])
            fillOrder(*i, visitedV, Stack);

    Stack.push(s);
}

// Print strongly connected component
void Graph::printSCC() {
    stack<int> Stack;
    bool* visitedV = new bool[V];
    for (int i = 0; i < V; i++)
        visitedV[i] = false;

    for (int i = 0; i < V; i++)
        if (visitedV[i] == false)
            fillOrder(i, visitedV, Stack);

    Graph gr = transpose();

    for (int i = 0; i < V; i++)
        visitedV[i] = false;
    int x = 0;
    while (Stack.empty() == false) {
        int s = Stack.top();
        Stack.pop();

        if (visitedV[s] == false) {
            x++;
            gr.DFS(s, visitedV);
            Quicksort(vec2, 0, vec2.size() - 1);
            for (int i = 0; i < vec.size();i++)
            {
                if (i == vec.size() - 1 && vec2.size() != 0)
                {
                    for (int j = 0; j < vec2.size();j++)
                    {
                        vec.push_back(vec2[j]);
                    }
                    vec2.clear();
                    vec.push_back(-1);
                    break;
                }
                else
                {
                    if (vec[i] == -1 && vec[i + 1] < vec2[0] && i != vec.size() - 1 && vec2.size() != 0)
                    {
                        vec.insert(vec.begin() + i + 1, -1);
                        for (int k = vec2.size() - 1; k >= 0;k--)
                        {
                            vec.insert(vec.begin() + i + 1, vec2[k]);
                        }
                        vec2.clear();
                    }
                }
            }
        }
    }
    cout << x << endl;
    for (int i = 1; i < vec.size() - 1;i++)
    {
        if (vec[i] == -1) cout << endl;
        else cout << vec[i] << " ";
    }
}


int main() {
    int n, k;
    cin >> n;
    cin >> k;
    Graph g(n);
    vec.push_back(-1);
    for (int i = 0;i < k;i++)
    {
        int a, b;
        cin >> a;
        cin >> b;
        g.addEdge(a, b);
    }

    g.printSCC();
}
