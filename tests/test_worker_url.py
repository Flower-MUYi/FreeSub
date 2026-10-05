import unittest

from vpngate import build_worker_url


class WorkerUrlTests(unittest.TestCase):
    def test_sstp_prefix_kept_and_host_port_encoded(self):
        base = "https://check.helei.kdns.fr/check?sstp=vpn:vpn@"
        url = build_worker_url(base, "1.2.3.4", 443)
        self.assertEqual(url, "https://check.helei.kdns.fr/check?sstp=vpn:vpn@1.2.3.4%3A443")
        self.assertEqual(url.count("vpn:vpn@"), 1)

    def test_placeholder_mode_also_encodes_target(self):
        base = "https://check.helei.kdns.fr/check?sstp=vpn:vpn@{target}"
        url = build_worker_url(base, "vpn123.opengw.net", 992)
        self.assertEqual(url, "https://check.helei.kdns.fr/check?sstp=vpn:vpn@vpn123.opengw.net%3A992")


if __name__ == "__main__":
    unittest.main()
