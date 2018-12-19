# dedis-cluster
redis-cluster plugin for django

基于redis-py-cluster,实现了使用redis集群作为django缓存的backend

### 安装

- 源码安装

```
git clone https://github.com/feiwencaho/dedis-cluster.git
cd dedis-cluster
python setup.py install
```

- pip安装

```
pip install dedis-cluster
```

### 使用
在settings.py中作如下配置
```python
CACHES = {
    'default': {
        'BACKEND': 'dedis_cluster.cache.RedisClusterCache',
        # your redis-cluster nodes
        "LOCATION": [
            "redis://192.168.1.4:7000/0",
            "redis://192.168.1.4:7001/0",
            "redis://192.168.1.4:7002/0",
            "redis://192.168.1.4:7003/0",
        ],
        'OPTIONS': {
            "CLIENT_CLASS": "dedis_cluster.client.DefaultClient",
        }
    }
}
```
