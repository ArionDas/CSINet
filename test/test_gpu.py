import torch
import spacy
import pytest

@pytest.mark.gpu
def test_torch():
    assert torch.cuda.is_available(), "Torch does not detect GPU"

@pytest.mark.gpu
def test_spacy():
    assert spacy.require_gpu(), "Spacy does not detect GPU"
