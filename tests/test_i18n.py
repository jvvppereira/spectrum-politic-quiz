import pytest
from src.core.i18n import load_locale, get_text, get_available_languages


class TestI18n:
    def test_pt_br_loads(self):
        locale = load_locale("pt_BR")
        assert "app_title" in locale
        assert locale["app_title"] == "Quiz Espectro Político"
    
    def test_en_us_loads(self):
        locale = load_locale("en_US")
        assert locale["app_title"] == "Political Spectrum Quiz"
    
    def test_get_text_pt_br(self):
        text = get_text("app_title", "pt_BR")
        assert text == "Quiz Espectro Político"
    
    def test_get_text_en_us(self):
        text = get_text("app_title", "en_US")
        assert text == "Political Spectrum Quiz"
    
    def test_fallback_to_pt_br(self):
        # Non-existent key falls back to pt_BR (which also won't have it, returns key)
        text = get_text("nonexistent_key_xyz", "en_US")
        assert text == "nonexistent_key_xyz"
    
    def test_get_available_languages(self):
        langs = get_available_languages()
        assert "pt_BR" in langs
        assert "en_US" in langs
        assert len(langs) == 2
    
    def test_all_keys_present_in_both(self):
        pt_br = load_locale("pt_BR")
        en_us = load_locale("en_US")
        
        # Both should have same keys
        assert set(pt_br.keys()) == set(en_us.keys())
        
        # Should have all question keys
        for i in range(1, 17):
            assert f"q{i}_theme" in pt_br
            assert f"q{i}_left" in pt_br
            assert f"q{i}_right" in pt_br
            assert f"q{i}_theme" in en_us
            assert f"q{i}_left" in en_us
            assert f"q{i}_right" in en_us
        
        # Should have all explanation keys
        for scale in ["behavioral", "economic", "general"]:
            for cls in ["left", "center_left", "center", "center_right", "right"]:
                key = f"explanation_{scale}_{cls}"
                assert key in pt_br
                assert key in en_us