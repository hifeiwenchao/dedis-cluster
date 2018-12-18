
class ConnectionInterrupted(Exception):
    """连接中断异常"""
    def __str__(self):
        error_type = self.__class__.__name__
        error_msg = "An error occurred while connecting to redis cluster"

        return "Redis Cluster %s: %s" % (error_type, error_msg)


class CompressorError(Exception):
    pass
