"""
Backend package for AI Life OS
"""

from .data_ingestion import load_google_fit_data
from .storage import store_data_locally

__all__ = ['load_google_fit_data', 'store_data_locally']