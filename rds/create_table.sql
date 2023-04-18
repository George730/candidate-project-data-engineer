drop table if exists `address`;
create table `address` (
    `street` varchar(128),
	`city` varchar(128) not null,
	`state` varchar(64) not null,
    `zip_code` varchar(32) not null,
    `role_profile_id` int,
    `address_id` int not null,
    `created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (address_id)
);

drop table if exists `email_type`;
create table `email_type` (
    `type` varchar(128) not null,
    `email_type_id` int not null,
    `created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (email_type_id)
);

drop table if exists `email`;
create table `email` (
    `value` varchar(20) not null,
    `email_type_id` int not null,
    `role_profile_id` int not null,
    `email_id` int not null,
    `created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (email_id)
);

drop table if exists `phone_number_type`;
create table `phone_number_type` (
    `type` varchar(128) not null,
    `phone_number_type_id` int not null,
    `created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (phone_number_type_id)
);

drop table if exists `phone_number`;
create table `phone_number` (
    `phone_number_type_id` int,
    `role_profile_id` int,
    `value` varchar(20) not null,
    `phone_number_id` int not null,
    `created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (phone_number_id)
);

drop table if exists `role_profile_type`;
create table `role_profile_type` (
    `type` varchar(128) not null,
    `role_profile_type_id` int not null,
    `created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (role_profile_type_id)
);

drop table if exists `role_profile`;
create table `role_profile` (
    `user_id` int,
    `role_profile_type_id` int,
    `role_profile_id` int not null,
    `created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (role_profile_id)
);

drop table if exists `user_profile`;
create table `user_profile` (
    `user_profile_id` varchar(128) not null,
    `first_name` varchar(128) not null,
    `last_name` varchar(128) not null,
    `created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (user_profile_id)
);

drop table if exists `users`;
create table `users` (
    `user_profile_id` varchar(128) not null,
	`user_id` int not null,
	`created` datetime not null,
    `created_by` varchar(128) not null,
    `updated` datetime,
    `updated_by` varchar(128)
	-- primary key (user_id)
);