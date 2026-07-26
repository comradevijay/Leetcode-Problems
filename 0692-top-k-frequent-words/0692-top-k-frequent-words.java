class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> map = new HashMap<>();

        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }

        List<String>[] bucket = new List[words.length + 1];
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            int frequency = entry.getValue();

            if (bucket[frequency] == null) {
                bucket[frequency] = new ArrayList<>();
            }

            bucket[frequency].add(entry.getKey());
        }

        List<String> answer = new ArrayList<>();
        for (int freq = words.length; freq >= 1; freq--) {
            if (bucket[freq] == null) {
                continue;
            }
            Collections.sort(bucket[freq]);

            for (String word : bucket[freq]) {
                answer.add(word);
                if (answer.size() == k) {
                    return answer;
                }
            }
        }

        return answer;
    }
}