"""Dockerhub tests."""

import os
from unittest import TestCase

import requests_mock  # pylint: disable=import-error

from repositoryupdater.dockerhub import DockerHub


def load_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        return fptr.read()


def dockerhub_url(name, version):
    """Dockerhub URL."""
    return "https://registry.hub.docker.com/v2/repositories/{}/tags/{}/".format(
        name,
        version,
    )


class TestDockerHub(TestCase):
    """Dockerhub test class."""

    @requests_mock.Mocker()
    def test_image_exists_on_dockerhub(self, mock):
        """Tests for image_exists_on_dockerhub()."""
        name = "package"
        version = "v1.0.0"
        mock.register_uri(
            requests_mock.ANY, dockerhub_url(name, version), text="Success"
        )

        # self.assertTrue(
        #     DockerHub.image_exists_on_dockerhub(name, version))
        self.assertFalse(DockerHub.image_exists_on_dockerhub(name, "nonexistent"))
