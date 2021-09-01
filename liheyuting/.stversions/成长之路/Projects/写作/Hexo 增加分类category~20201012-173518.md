title: Hexo 增加分类category
date: 2020-7-5
categories：
- 研究创作
tags:
- learn
- blog
---

# hexo中配置category
1. 进入博客地址，执行命令
`hexo new page cotegories`

2. 在categories中增加type
```
---
title: 文章分类
date: 2020-07-05 19:36:03
type: "categories"
comments: false
---
```

3. 给文章中增加categories
```
title: Hexo 增加分类category
date: 2020-7-5
categories：
- 研究创作
tags:
- learn
- blog
```

即添加`categories: xxx`

4. 在首页中显示category
设置theme中的`_config.yml`中的` categories: /categories/ || th`显示出来


5. 配置文件夹
blog`_config.yml`中有category_dir: categories




# 我如何设置category
这个想聊一聊目前我是怎么




