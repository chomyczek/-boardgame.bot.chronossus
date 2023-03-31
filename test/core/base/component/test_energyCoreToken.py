from src.core.base.component.energyCoreToken import EnergyCoreToken


class TestEnergyCoreToken:
    def test_init(self):
        is_exhausted = True
        exhausted_core = EnergyCoreToken(is_exhausted)
        not_exhausted_core = EnergyCoreToken()
        assert exhausted_core.is_exhausted
        assert not not_exhausted_core.is_exhausted
