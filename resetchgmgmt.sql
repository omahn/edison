BEGIN;
DROP TABLE `changemanagement_changeheader_AffectedItems`;
DROP TABLE `changemanagement_details`;
DROP TABLE `changemanagement_changeheader`;
DROP TABLE `changemanagement_scmrepo`;
DROP TABLE `changemanagement_scmtype`;
DROP TABLE `changemanagement_changestatus`;
CREATE TABLE `changemanagement_changestatus` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `Description` varchar(128) NOT NULL,
    `ClosesChangeRequest` bool NOT NULL
)
;
CREATE TABLE `changemanagement_scmtype` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `Name` varchar(50) NOT NULL,
    `LibraryName` varchar(255) NOT NULL
)
;
CREATE TABLE `changemanagement_scmrepo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `Scm_id` integer NOT NULL,
    `Url` varchar(255) NOT NULL,
    `Name` varchar(255) NOT NULL,
    `Description` varchar(255) NOT NULL
)
;
ALTER TABLE `changemanagement_scmrepo` ADD CONSTRAINT `Scm_id_refs_id_5e096793` FOREIGN KEY (`Scm_id`) REFERENCES `changemanagement_scmtype` (`id`);
CREATE TABLE `changemanagement_changeheader` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `Title` varchar(255) NOT NULL,
    `Requestor_id` integer NOT NULL,
    `Summary` longtext NOT NULL,
    `ScmRepo_id` integer NOT NULL,
    `Created` date NOT NULL,
    `Due` datetime NOT NULL,
    `Status_id` integer NOT NULL,
    `Completed` bool NOT NULL
)
;
ALTER TABLE `changemanagement_changeheader` ADD CONSTRAINT `Requestor_id_refs_id_12d87342` FOREIGN KEY (`Requestor_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `changemanagement_changeheader` ADD CONSTRAINT `ScmRepo_id_refs_id_54c8d224` FOREIGN KEY (`ScmRepo_id`) REFERENCES `changemanagement_scmrepo` (`id`);
ALTER TABLE `changemanagement_changeheader` ADD CONSTRAINT `Status_id_refs_id_4c79ccec` FOREIGN KEY (`Status_id`) REFERENCES `changemanagement_changestatus` (`id`);
CREATE TABLE `changemanagement_details` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `Header_id` integer NOT NULL,
    `Description` longtext NOT NULL,
    `GitCommit` varchar(255) NOT NULL,
    `Created` datetime NOT NULL,
    `UpdatedBy_id` integer NOT NULL
)
;
ALTER TABLE `changemanagement_details` ADD CONSTRAINT `Header_id_refs_id_f62d0e1f` FOREIGN KEY (`Header_id`) REFERENCES `changemanagement_changeheader` (`id`);
ALTER TABLE `changemanagement_details` ADD CONSTRAINT `UpdatedBy_id_refs_id_db5912f6` FOREIGN KEY (`UpdatedBy_id`) REFERENCES `auth_user` (`id`);
CREATE TABLE `changemanagement_changeheader_AffectedItems` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `changeheader_id` integer NOT NULL,
    `configurationitem_id` integer NOT NULL,
    UNIQUE (`changeheader_id`, `configurationitem_id`)
)
;
ALTER TABLE `changemanagement_changeheader_AffectedItems` ADD CONSTRAINT `changeheader_id_refs_id_5a3703d4` FOREIGN KEY (`changeheader_id`) REFERENCES `changemanagement_changeheader` (`id`);
ALTER TABLE `changemanagement_changeheader_AffectedItems` ADD CONSTRAINT `configurationitem_id_refs_id_55c18e90` FOREIGN KEY (`configurationitem_id`) REFERENCES `cmdb_configurationitem` (`id`);
CREATE INDEX `changemanagement_scmrepo_Scm_id` ON `changemanagement_scmrepo` (`Scm_id`);
CREATE INDEX `changemanagement_changeheader_Requestor_id` ON `changemanagement_changeheader` (`Requestor_id`);
CREATE INDEX `changemanagement_changeheader_ScmRepo_id` ON `changemanagement_changeheader` (`ScmRepo_id`);
CREATE INDEX `changemanagement_changeheader_Status_id` ON `changemanagement_changeheader` (`Status_id`);
CREATE INDEX `changemanagement_details_Header_id` ON `changemanagement_details` (`Header_id`);
CREATE INDEX `changemanagement_details_UpdatedBy_id` ON `changemanagement_details` (`UpdatedBy_id`);
COMMIT;
