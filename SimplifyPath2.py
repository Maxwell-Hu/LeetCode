class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirname_list = [dirname for dirname in path.split('/') if dirname != '' and dirname != '.']
        stack = []
        for dirname in dirname_list:
            if dirname == '..':
                if len(stack):
                    stack.pop()
            else:
                stack.append(dirname)
        return '/' + '/'.join(stack)
