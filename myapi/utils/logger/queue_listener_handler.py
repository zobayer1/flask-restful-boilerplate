# -*- coding: utf-8 -*-
import atexit
from logging.config import ConvertingDict, ConvertingList, valid_ident
from logging.handlers import QueueHandler, QueueListener
from typing import Any


class QueueListenerHandler(QueueHandler):  # pragma: no cover
    def __init__(self, handlers: Any, queue: Any, respect_handler_level: bool = True, auto_run: bool = True):
        queue = self._resolve_queue(queue)
        handlers = self._resolve_handlers(handlers)
        super().__init__(queue)
        self._listener = QueueListener(queue, *handlers, respect_handler_level=respect_handler_level)
        if auto_run:
            self._listener.start()
            atexit.register(self._listener.stop)

    def emit(self, payload):
        return super().emit(payload)

    @staticmethod
    def _resolve_queue(queue: Any):
        if not isinstance(queue, ConvertingDict):
            return queue
        if "__resolved_value__" in queue:
            return queue["__resolved_value__"]
        cname = queue.pop("class")
        klass = queue.configurator.resolve(cname)
        props = queue.pop(".", None)
        kwargs = {k: queue[k] for k in queue if valid_ident(k)}
        result = klass(**kwargs)
        if props:
            for name, value in props.items():
                setattr(result, name, value)
        queue["__resolved_value__"] = result
        return result

    @staticmethod
    def _resolve_handlers(handlers: Any):
        if not isinstance(handlers, ConvertingList):
            return handlers
        return [handlers[i] for i in range(len(handlers))]
