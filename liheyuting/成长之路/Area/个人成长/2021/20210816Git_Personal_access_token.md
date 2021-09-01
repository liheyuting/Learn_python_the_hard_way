title: Git Personal access token更新
date: 2021-08-16 16:51
categories:
- 工具
tags:
- Git
- obsidian
---

去年GitHub就不停发邮件提醒之后不能用账号密码远程同步repo了，懒惰的我一直没当回事，然后8月13日开始它就真的啥也不管直接停用。。

第一步，我尝试了下在GitHub平台设置了personal access token，路径如下，这个密码一定要先copy下来，要不然之后再也看不到了（因为这个我建了好几次。。心累）

![](Pasted%20image%2020210816165507.png)

接着先通过命令行，清除了历史的账号密码

```
git config --global credential.helper cache
#可以更改默认的密码缓存时限
git config --global credential.helper 'cache --timeout=3600'
```

或者：
![](Pasted%20image%2020210816165632.png)

第三步，我就开始了命令行不停的输入账号和tokes密码（tokes那串作为账号密码使用），不停的失败。。

放弃，我在github客户端打开，使用了同样的命令，让输密码时，选择输入了tokes一串数字，然后成功了 :)

峰回路转。。

不管怎样，成功了就好。