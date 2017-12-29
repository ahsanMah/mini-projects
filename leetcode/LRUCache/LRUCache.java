import java.util.*;

class LRUCache {
    
    private class CacheEntry{
        int value;
        int priority;
        
        public CacheEntry(int value, int priority){
            this.value = value;
            this.priority = priority;
        }
        
    }

    
    HashMap<Integer,Integer> cache;
    PriorityQueue<CacheEntry> LRU;
    int capacity;
    
    public LRUCache(int capacity) {
        this.cache = new HashMap<Integer,Integer>(capacity);
        this.capacity = capacity;
    }
    
    public int get(int key) {
        return 1;
    }
    
    public void put(int key, int value) {
        
    }
    
    public static void main(String[] args){
        LRUCache cache = new LRUCache( 2 /* capacity */ );
        cache.put(1, 1);
        cache.put(2, 2);
        System.out.println(cache.get(1));       // returns 1
        cache.put(3, 3);    // evicts key 2
        cache.get(2);       // returns -1 (not found)
        cache.put(4, 4);    // evicts key 1
        cache.get(1);       // returns -1 (not found)
        cache.get(3);       // returns 3
        cache.get(4);       // returns 4
    }
    
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */


