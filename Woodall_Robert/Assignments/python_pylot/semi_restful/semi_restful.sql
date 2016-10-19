-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema semi_restful
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema semi_restful
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `semi_restful` DEFAULT CHARACTER SET utf8 ;
USE `semi_restful` ;

-- -----------------------------------------------------
-- Table `semi_restful`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `semi_restful`.`Product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `price` DECIMAL(10,2) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
