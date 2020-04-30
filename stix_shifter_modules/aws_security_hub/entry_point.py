from stix_shifter_utils.utils.entry_point_base import EntryPointBase

class EntryPoint(EntryPointBase):

    def __init__(self, options):
        super().__init__(options)
        #TODO add transmission tests
        #TODO add translation tests
        if connection and configuration:
            self.setup_transmission_basic(connection, configuration)
        else:
            self.setup_translation_simple('default', query_translator=QueryTranslator())