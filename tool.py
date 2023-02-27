#-*- coding:utf-8 -*-

# ����
config = {
    "width" : 150,   # ��������
    "height" : 100,  # �����߶�
    "frame" : 10,    # ���ŵ�֡��
    "ratio" : 1.0,   # ͼ�����ŵı���
}

# ��ҳcss��ʽ
Style = '''
<style>
    .div-a > pre {font-size : 6px; line-height : 2px; }
    .div-a {float : left; width : 69%;}
    .div-b {float : left; width : 29%;}
</style>
'''

# javascript���룬�����ʾpre������ַ�
JavaScript = '''
<script>
    window.onload = function(){
        var frames = document.getElementsByTagName('pre');
        var length = frames.length;
        var current = 0;
        var doframe = function() {
            frames[current].style.display = 'block';
            frames[(current - 1 + length) %% length].style.display = 'none';
            current = (current + 1) %% length;
        }
        for (var i = 0; i < length; i++)
            frames[i].style.display = 'none';
        setInterval(doframe, 1000/%d)
    }
</script>
''' % config['frame']
