class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirname_list = [dirname for dirname in path.split('/') if dirname != '' and dirname != ',']
        while '..' in dirname_list:
            idx = dirname_list.index('..')
            dirname_list.remove(dirname_list[idx])
            if idx : dirname_list = dirname_list[:idx-1] + dirname_list[idx:]
        return '/' + '/'.join(dirname_list)
