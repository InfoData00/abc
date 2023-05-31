#include<iostream>
#include<queue>
#include<map>
#include<vector>
using namespace std;

void BFS(map<int,vector<int>>&graph,int startnode)
{
    map<int,bool>visited;

    queue<int>bfsQueue;

    visited[startnode]=true;
    bfsQueue.push(startnode);

    while(!bfsQueue.empty())
    {
        int currentnode= bfsQueue.front();
        bfsQueue.pop();
        cout<< currentnode<<" ";

        vector<int> neighbors= graph[currentnode];

        for(int i=0;i<neighbors.size();++i)
        {
            int neighbor=neighbors[i];
            if(!visited[neighbor])
            {
                visited[neighbor]=true;
                bfsQueue.push(neighbor);
            }
        }
    }
}

int main()
{
   int numedge,startnode;
   cout<<"Enter the size of edges";
   cin >>numedge;
   
   map<int,vector<int>>graph;
   cout<<"enter the edges:\n";

   for(int i=0;i<numedge;i++)
   {
      int u,v;
      cin>>u>>v;
      graph[u].push_back(v);
      graph[v].push_back(u);
    
   }
     cout<<"Enter the starting node";
     cin>>startnode;

     cout<<"starting from node"<<startnode<<" : ";
      BFS(graph,startnode);
}