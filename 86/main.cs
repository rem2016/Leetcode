    public class Solution
    {
        public ListNode Partition(ListNode head, int x)
        {
            if (head == null)
            {
                return head;
            }
            ListNode pre = null, firstGreater = null, node = head;
            while (node != null)
            {
                if (node.val >= x)
                {
                    firstGreater = node;
                    break;
                }
                pre = node;
                node = node.next;
            }
            if (firstGreater == null)
            {
                return head;
            }
            ListNode lastGreater = null;
            while (node != null)
            {
                if (node.val < x)
                {
                    lastGreater.next = node.next;
                    if (pre == null)
                    {
                        pre = node;
                        head = node;
                    }
                    else
                    {
                        pre.next = node;
                        pre = node;
                    }
                    node.next = firstGreater;
                }
                else
                {
                    lastGreater = node;
                }
                node = node.next;
            }
            return head;
        }
    }

