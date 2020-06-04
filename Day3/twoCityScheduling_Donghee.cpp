class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        vector<int> diff(); // difference = A - B
        
        priority_queue<pair<int, int> > pq; 
        
        int personId = 0;
        for (vector<int>& pr : costs) {
            pq.push(make_pair(pr[0] - pr[1], personId++));
        }
        
        int count = 0, limit = costs.size() / 2;
        int res = 0;
        
        while (count < limit) {
            // pq.top().second is the personID of a person we should schedule to B rather than A
            res += costs[pq.top().second][1];           
            count++;
            pq.pop();
        }
        
        while (!pq.empty()) {
            res += costs[pq.top().second][0];
            pq.pop();
        }
        
        return res;
    }
};