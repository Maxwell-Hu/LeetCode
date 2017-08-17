class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirname_list = path.split('/')
        while '' in dirname_list:
            dirname_list.remove('')
        while '.' in dirname_list:
            dirname_list.remove('.')
        while '..' in dirname_list:
            idx = dirname_list.index('..')
            dirname_list.remove(dirname_list[idx])
            if idx : dirname_list = dirname_list[:idx-1] + dirname_list[idx:]
        return '/' + '/'.join(dirname_list)
