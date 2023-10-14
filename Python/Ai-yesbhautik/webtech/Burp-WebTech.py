# Burp WebTech Extension

from burp import (IBurpExtender, IScannerCheck, IScanIssue, ITab)
from java.net import URL
from javax.swing import (GroupLayout, JPanel, JCheckBox, JButton)
import pickle
import json
from webtech import WebTech
from webtech.__version__ import __version__ as VERSION

issueTypeWebTech = 3933012
issueNameWebTech = "Detected some technologies in use"

class BurpExtender(IBurpExtender, IScannerCheck, IScanIssue, ITab):
    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("WebTech")
        self.out = callbacks.getStdout()
        self.callbacks.printOutput("Sucessfully loaded WebTech {}".format(VERSION))

        self.webtech = WebTech(options={'json': True})

        # define all checkboxes
        self.cbPassiveChecks = self.defineCheckBox("Enable Passive Scanner Checks")
        self.cbActiveChecks = self.defineCheckBox("Enable Active Scanner Checks", True, False)
        self.btnSave = JButton("Set as default", actionPerformed=self.saveConfig)
        self.btnRestore = JButton("Restore", actionPerformed=self.restoreConfig)
        self.grpConfig = JPanel()
        self.grpConfig.add(self.btnSave)
        self.grpConfig.add(self.btnRestore)
        self.restoreConfig()

        # definition of config tab
        self.tab = JPanel()
        layout = GroupLayout(self.tab)
        self.tab.setLayout(layout)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)
        layout.setHorizontalGroup(
            layout.createSequentialGroup()
            .addGroup(layout.createParallelGroup()
                      .addComponent(self.cbPassiveChecks)
                      .addComponent(self.cbActiveChecks)
                      )
            .addGroup(layout.createParallelGroup()
                      .addComponent(self.grpConfig, GroupLayout.PREFERRED_SIZE, GroupLayout.PREFERRED_SIZE, GroupLayout.PREFERRED_SIZE)
                      )
        )
        layout.setVerticalGroup(
            layout.createSequentialGroup()
            .addComponent(self.cbPassiveChecks)
            .addComponent(self.cbActiveChecks)
            .addComponent(self.grpConfig, GroupLayout.PREFERRED_SIZE, GroupLayout.PREFERRED_SIZE, GroupLayout.PREFERRED_SIZE)
        )

        callbacks.registerScannerCheck(self)
        callbacks.addSuiteTab(self)

    def defineCheckBox(self, caption, selected=True, enabled=True):
        checkBox = JCheckBox(caption)
        checkBox.setSelected(selected)
        checkBox.setEnabled(enabled)
        return checkBox

    def saveConfig(self, e=None):
        config = {
            'PassiveChecks': self.cbPassiveChecks.isSelected(),
            'ActiveChecks': self.cbActiveChecks.isSelected(),
        }
        self.callbacks.saveExtensionSetting("config", pickle.dumps(config))

    def restoreConfig(self, e=None):
        storedConfig = self.callbacks.loadExtensionSetting("config")
        if storedConfig is not None:
            try:
                config = pickle.loads(storedConfig)
                self.cbPassiveChecks.setSelected(config['PassiveChecks'])
                self.cbActiveChecks.setSelected(config['ActiveChecks'])
            except:
                self.callbacks.printOutput("Something went wrong with config restore.\nConfig contained: " + storedConfig)

    ### ITab ###
    def getTabCaption(self):
        return("WebTech")

    def getUiComponent(self):
        return self.tab

    ### IScannerCheck ###
    def doPassiveScan(self, baseRequestResponse):
        if not self.cbPassiveChecks.isSelected():
            return None

        scanIssues = list()

        analyzedResponse = self.helpers.analyzeResponse(baseRequestResponse.getResponse())

        # Filter responses for code 200 and content-type text/html
        # We are only interested in code 200 html or other status codes
        if analyzedResponse.getInferredMimeType() != 'HTML':
            return None

        req = baseRequestResponse.getRequest().tostring()
        resp = baseRequestResponse.getResponse().tostring()
        exchange = {'request': req, 'response': resp}

        wt_report = self.webtech.start_from_exchange(exchange)
        if wt_report.get('tech') is None or wt_report.get('headers') is None or (wt_report['tech'] == [] and wt_report['headers'] == []):
            # there was a fail or nothing was detected
            return None

        scanIssues.append(WebTechScanIssue(
            baseRequestResponse,
            wt_report,
            self.helpers,
            self.callbacks
        ))

        return scanIssues

    def consolidateDuplicateIssues(self, existingIssue, newIssue):
        """
        This function is called on multiple Issue with same URL
        """
        if newIssue.getIssueName() == issueNameWebTech and existingIssue.getIssueName() == newIssue.getIssueName():
            if existingIssue.getIssueDetail() == newIssue.getIssueDetail():
                # Same tech detected, always skip
                return -1
        return 0


class WebTechScanIssue(IScanIssue):
    def __init__(self, requestResponse, wt_report, helpers, callbacks):
        self.requestResponse = requestResponse
        analyzedRequest = helpers.analyzeRequest(requestResponse)
        self.findingUrl = analyzedRequest.getUrl()
        self.report = wt_report

    def getUrl(self):
        return self.findingUrl

    def getIssueName(self):
        return issueNameWebTech

    def getIssueType(self):
        return issueTypeWebTech

    def getSeverity(self):
        return "Information"

    def getConfidence(self):
        return "Certain"

    def getIssueBackground(self):
        return None

    def getRemediationBackground(self):
        return None

    def getIssueDetail(self):
        msg = "WebTech detected some technologies or custom headers in use on this website.<br><br><br>"

        techs = self.report['tech']
        if len(techs) > 0:
            msg += "Detected the following Technologies:<br>"
            tmpl = " - {} {}<br>"
            for tech in sorted(techs):
                msg += tmpl.format(tech['name'], tech['version'] if tech['version'] is not None else '')

        headers = self.report['headers']
        if len(headers) > 0:
            msg += "<br><br>Detected the following Custom Headers:<br>"
            tmpl = " - {}: {}<br>"
            for header in sorted(headers):
                msg += tmpl.format(header['name'], header['value'])

        return msg

    def getRemediationDetail(self):
        return None

    def getHttpMessages(self):
        return [self.requestResponse]

    def getHttpService(self):
        return self.requestResponse.getHttpService()


def baseurl(url):
    parts = url.split('/')
    return '/'.join(parts[:-1]) + '/'
