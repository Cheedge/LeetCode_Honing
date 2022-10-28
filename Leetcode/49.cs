public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, IList<string>> dict = new Dictionary<string, IList<string>>();
        foreach (string it in strs) {
            // sort every str item in strs
            char[] its = it.ToCharArray();
            Array.Sort(its);
            // string chars = it.ToString();
            string chars = new string(its);
            // Console.WriteLine(chars);
            // Console.WriteLine(dict.ContainsKey(chars));
            // List<char> sortedStr = chars;
            // compared with dict
            // if exist add to that list
            // if not add a new key
            if (dict.ContainsKey(chars)) {
                // Array.Add(dict[chars], it);
                dict[chars].Add(it);
                // dict[chars].Select(i=>$"{i}").ToList().ForEach(Console.WriteLine);
            }else{
                dict[chars] = new List<string>();
                dict[chars].Add(it);
                // Console.WriteLine(dict.ContainsKey(chars));
                // dict[chars].Select(i=>$"{i}").ToList().ForEach(Console.WriteLine);
            }
            // dict[chars].Add(it);
        }
        // get all the vals in the dict
        IList<IList<string>> res = new List<IList<string>>();
        foreach (IList<string> v in dict.Values) {
            // v.Select(i=>$"{i}").ToList().ForEach(Console.WriteLine);
            // Console.WriteLine("***");
            res.Add(v);
        }
        // dict.Select(i => $"{i.Key}: {i.Value}").ToList().ForEach(Console.WriteLine);
        // Console.WriteLine(Serialize(dict.ToList()));
        return res;
    }
}