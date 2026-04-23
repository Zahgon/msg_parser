# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Based on MS-OXMSG protocol specification
# ref: https://blogs.msdn.microsoft.com/openspecification/2010/06/20/msg-file-format-rights-managed-email-message-part-2/
# ref: https://msdn.microsoft.com/en-us/library/cc463912(v=EXCHG.80).aspx
import email
import os
import re
from pickle import dumps
from struct import unpack

from olefile import OleFileIO
from olefile import isOleFile

from .data_models import DataModel
from .email_builder import EmailFormatter
from .properties.ms_props_id_map import PROPS_ID_MAP

TOP_LEVEL_HEADER_SIZE = 32
RECIPIENT_HEADER_SIZE = 8
ATTACHMENT_HEADER_SIZE = 8
EMBEDDED_MSG_HEADER_SIZE = 24
CONTROL_CHARS = re.compile(r"[\n\r\t]")


class Message(object):
    """
     Class to store Message properties
    """

    def __init__(self, directory_entries):

        self._streams = self._process_directory_entries(directory_entries)
        self._data_model = DataModel()
        self._nested_attachments_depth = 0
        self.properties = self._get_properties()
        self.attachments = self._get_attachments()
        self.recipients = self._get_recipients()

    def as_dict(self):
        """
        returns message attributes as a python dictionary.
        :return: dict
        """
        pass

    def _set_property_stream_info(self, ole_file, header_size):
        pass

    @staticmethod
    def _process_directory_entries(directory_entries):

        pass

    def _get_properties(self):

        pass

    def _get_recipients(self):

        pass

    def _get_attachments(self):
        pass

    def _get_property_data(self, directory_name, directory_entry, is_list=False):
        pass

    @staticmethod
    def _get_canonical_property_name(dir_entry_name):
        pass

    def __repr__(self):
        return "Message [%s]" % self.properties.get(
            "InternetMessageId", self.properties.get("Subject")
        )


class Recipient(object):
    """
     class to store recipient attributes
    """

    def __init__(self, recipients_properties):
        self.AddressType = recipients_properties.get("AddressType")
        self.Account = recipients_properties.get("Account")
        self.EmailAddress = recipients_properties.get("SmtpAddress")
        self.DisplayName = recipients_properties.get("DisplayName")
        self.ObjectType = recipients_properties.get("ObjectType")
        self.RecipientType = recipients_properties.get("RecipientType")

    def __repr__(self):
        return "%s (%s)" % (self.DisplayName, self.EmailAddress)


class Attachment(object):
    """
     class to store attachment attributes
    """

    def __init__(self, attachment_properties):

        self.DisplayName = attachment_properties.get("DisplayName")
        self.AttachEncoding = attachment_properties.get("AttachEncoding")
        self.AttachContentId = attachment_properties.get("AttachContentId")
        self.AttachMethod = attachment_properties.get("AttachMethod")
        self.AttachmentSize = format_size(attachment_properties.get("AttachmentSize"))
        self.AttachFilename = attachment_properties.get("AttachFilename")
        self.AttachLongFilename = attachment_properties.get("AttachLongFilename")
        if self.AttachLongFilename:
            self.Filename = self.AttachLongFilename
        else:
            self.Filename = self.AttachFilename
        if self.Filename:
            self.Filename = os.path.basename(self.Filename)
        else:
            self.Filename = "[NoFilename_Method%s]" % self.AttachMethod
        self.data = attachment_properties.get("AttachDataObject")
        self.AttachMimeTag = attachment_properties.get(
            "AttachMimeTag", "application/octet-stream"
        )
        self.AttachExtension = attachment_properties.get("AttachExtension")

    def __repr__(self):
        return "%s (%s / %s)" % (
            self.Filename,
            self.AttachmentSize,
            len(self.data or []),
        )


class MsOxMessage(object):
    """
     Base class for Microsoft Message Object
    """

    def __init__(self, msg_file_path):
        self.msg_file_path = msg_file_path
        self.include_attachment_data = False

        if not self.is_valid_msg_file():
            raise Exception(
                "Invalid file provided, please provide valid Microsoft’s Outlook MSG file."
            )

        with OleFileIO(msg_file_path) as ole_file:
            # process directory entries
            ole_root = ole_file.root
            kids_dict = ole_root.kids_dict

            self._message = Message(kids_dict)
            self._message_dict = self._message.as_dict()

            # process msg properties
            self._set_properties()

            # process msg recipients
            self._set_recipients()

            # process attachments
            self._set_attachments()

    def get_properties(self):

        pass

    def get_properties_as_dict(self):
        pass

    def get_message_as_json(self):
        try:
            if not self.include_attachment_data:
                for _, attachment in self._message_dict.get("attachments", []).items():
                    if not isinstance(attachment, dict):
                        continue
                    attachment["AttachDataObject"] = {}
            # Using Pickle to encode message. There is bytes-like objects in it. Therefore cannot be treated by embed json.dumps method
            json_string = dumps(self._message_dict)
            return json_string
        except ValueError:
            return None

    def get_email_mime_content(self):
        pass

    def save_email_file(self, file_path, file_name=None):
        email_obj = EmailFormatter(self)
        email_obj.save_file(file_path, file_name)
        return True

    def _set_properties(self):
        pass

    def _set_recipients(self):
        pass

    def _set_attachments(self):
        pass

    def is_valid_msg_file(self):
        pass


def format_size(num, suffix="B"):
    pass


def parse_email_headers(header, raw=False):
    pass
