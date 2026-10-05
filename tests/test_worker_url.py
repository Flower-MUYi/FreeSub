import unittest

from vpngate import build_worker_url


class WorkerUrlTests(unittest.TestCase):
    def test_sstp_prefix_kept_and_host_port_encoded(self):
        base = "https://freesub.pinemuyi.workers.dev/check?sstp=vpn:vpn@"
        url = build_worker_url(base, "public-vpn-124.opengw.net", 443)
        self.assertEqual(
            url,
            "https://freesub.pinemuyi.workers.dev/check?sstp=vpn:vpn@public-vpn-124.opengw.net%3A443",
        )
        self.assertEqual(url.count("vpn:vpn@"), 1)

    def test_placeholder_mode_also_encodes_target(self):
        base = "https://freesub.pinemuyi.workers.dev/check?sstp=vpn:vpn@{target}"
        url = build_worker_url(base, "vpn123.opengw.net", 992)
        self.assertEqual(
            url,
            "https://freesub.pinemuyi.workers.dev/check?sstp=vpn:vpn@vpn123.opengw.net%3A992",
        )


if __name__ == "__main__":
    unittest.main()
