from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.nlu.components import Component

import typing
from typing import Any, Optional, Text, Dict

@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.MESSAGE_TOKENIZER, is_trainable=False
)

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


    class DeleteSymbols(GraphComponent, Component):

        provides = ["text"]
        #requires = []
        defaults = {}
        language_list = None

        def __init__(self, component_config=None):
            super(DeleteSymbols, self).__init__(component_config)

        def train(self, training_data, cfg, **kwargs):
            pass

        def process(self, message, **kwargs):
            mt =  message.text
            message.text = mt.translate(mt.maketrans('', '', '-$%&(){}^'))

        def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
            pass

        @classmethod
        def load(
            cls,
            meta: Dict[Text, Any],
            model_dir: Optional[Text] = None,
            model_metadata: Optional["Metadata"] = None,
            cached_component: Optional["Component"] = None,
            **kwargs: Any
        ) -> "Component":
            """Load this component from file."""

            if cached_component:
                return cached_component
            else:
                return cls(meta)
        def create(
            cls,
            config: Dict[Text, Any],
            model_storage: ModelStorage,
            resource: Resource,
            execution_context: ExecutionContext,
        ) -> GraphComponent:
            return cls(config)
        
        @staticmethod
        def get_default_config() -> Dict[Text, Any]:
            return {"key1": "value1"}